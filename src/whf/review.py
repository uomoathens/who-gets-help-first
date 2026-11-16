from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np

from .config import Config
from .expand import expand
from .metrics import krippendorff_interval
from .prompts import build
from .run import load_study

SHEET = "Αξιολόγηση"
YES, NO = "Ναι", "Όχι"
COLUMNS = [
    ("Α/Α", 6),
    ("Κωδικός", 26),
    ("Σενάριο (Ελληνικά)", 90),
    ("Scenario (English)", 90),
    ("Αίτημα προς κρίση", 14),
    ("Ρεαλισμός (1-5)", 14),
    ("Επάρκεια πληροφοριών (1-5)", 16),
    ("Προκύπτει σαφώς η προτεραιότητά του; (Ναι/Όχι)", 20),
    ("Σχόλια", 40),
]
INSTRUCTIONS = [
    "Οδηγίες προς τον αξιολογητή",
    "",
    "Στο φύλλο «Αξιολόγηση» υπάρχουν {n} σενάρια αντιμετώπισης πλημμύρας, το καθένα στα Ελληνικά και στα Αγγλικά. Είναι ακριβώς το κείμενο που δόθηκε στα γλωσσικά μοντέλα, χωρίς την οδηγία για τη μορφή της απάντησης.",
    "Παρακαλούμε να συμπληρώσετε για κάθε σενάριο τις στήλες F έως I, ανεξάρτητα από τον άλλο αξιολογητή. Η στήλη E δείχνει το αίτημα του σεναρίου που μας ενδιαφέρει (με το γράμμα του).",
    "",
    "Ρεαλισμός (1-5): πόσο πιθανό είναι να προκύψει ένα τέτοιο αίτημα σε πραγματική επιχείρηση πολιτικής προστασίας. 1 = καθόλου, 5 = απολύτως.",
    "Επάρκεια πληροφοριών (1-5): αν οι πληροφορίες αρκούν για να ληφθεί απόφαση. 1 = καθόλου, 5 = απολύτως.",
    "Προκύπτει σαφώς η προτεραιότητά του; Ναι, αν από τα στοιχεία (βάθος νερού, αριθμός ανθρώπων, χρόνος αναμονής, ζημιές ή ημέρες χωρίς νερό) είναι σαφές ποια αιτήματα προηγούνται του αιτήματος της στήλης E και ποια έπονται (ή, όταν υπάρχει μόνο μία αίτηση, αν είναι σαφώς υψηλής ή σαφώς χαμηλής προτεραιότητας)· Όχι, αν τα κριτήρια δείχνουν σε διαφορετικές κατευθύνσεις.",
    "Σχόλια: οτιδήποτε μη ρεαλιστικό, ασαφές ή λανθασμένο.",
    "",
    "Μην αλλάζετε τις στήλες A έως E. Αποθηκεύστε το αρχείο με το όνομά σας, για παράδειγμα reviews/expert-a.xlsx.",
]


def _prompt(case, attributes, prompts, lang: str):
    return build(case, expand(case, attributes)[0], lang, 0, prompts.roles()[0], 0, attributes, prompts)


def scenario_text(case, attributes, prompts, lang: str) -> str:
    text = _prompt(case, attributes, prompts, lang).messages[1]["content"]
    parts = [p for p in text.split("\n\n") if p.strip()]
    return "\n\n".join(parts[:-1]) if len(parts) > 1 else text


def target_label(case, attributes, prompts) -> str:
    if len(case.units) == 1:
        return "Μοναδική αίτηση"
    return next(label for label, uid in _prompt(case, attributes, prompts, "el").labels if uid == case.target)


def sample_cases(cases: list, per_task: int, seed: int) -> list:
    rng = np.random.default_rng(seed)
    out = []
    for task in sorted({c.task for c in cases}):
        by_setting = {}
        for c in cases:
            if c.task == task:
                by_setting.setdefault(c.setting, []).append(c)
        settings = sorted(by_setting)[:per_task]
        combos = [combo for combo in itertools.product(*(by_setting[s] for s in settings))
                  if len({c.clarity for c in combo}) > 1 or len({c.clarity for c in cases if c.task == task}) == 1]
        out.extend(combos[int(rng.integers(len(combos)))])
    return out


def make_sheet(cfg: Config, path: Path, per_task: int = 3) -> list:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation

    attributes, prompts, cases = load_study(cfg)
    chosen = sample_cases(cases, per_task, cfg.seed)
    wb = Workbook()
    info = wb.active
    info.title = "Οδηγίες"
    for i, line in enumerate(INSTRUCTIONS, start=1):
        cell = info.cell(row=i, column=1, value=line.format(n=len(chosen)))
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    info["A1"].font = Font(bold=True, size=13)
    info.column_dimensions["A"].width = 120
    ws = wb.create_sheet(SHEET)
    head = PatternFill("solid", fgColor="1F4E79")
    for j, (name, width) in enumerate(COLUMNS, start=1):
        cell = ws.cell(row=1, column=j, value=name)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = head
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[cell.column_letter].width = width
    ws.row_dimensions[1].height = 45
    ws.freeze_panes = "C2"
    for i, c in enumerate(chosen, start=2):
        values = [i - 1, c.id, scenario_text(c, attributes, prompts, "el"), scenario_text(c, attributes, prompts, "en"),
                  target_label(c, attributes, prompts)]
        for j, v in enumerate(values, start=1):
            ws.cell(row=i, column=j, value=v).alignment = Alignment(wrap_text=True, vertical="top")
        for j in range(6, 10):
            ws.cell(row=i, column=j).alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[i].height = 260
    last = len(chosen) + 1
    scale = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True)
    scale.error = "Ακέραιος από 1 έως 5"
    yesno = DataValidation(type="list", formula1=f'"{YES},{NO}"', allow_blank=True)
    ws.add_data_validation(scale)
    ws.add_data_validation(yesno)
    scale.add(f"F2:G{last}")
    yesno.add(f"H2:H{last}")
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return [c.id for c in chosen]


def read_sheet(path: Path) -> dict:
    from openpyxl import load_workbook

    ws = load_workbook(path, data_only=True)[SHEET]
    out = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not row or not row[1]:
            continue
        realism, sufficiency, clear = row[5], row[6], row[7]
        out[str(row[1])] = dict(
            realism=float(realism) if isinstance(realism, (int, float)) else np.nan,
            sufficiency=float(sufficiency) if isinstance(sufficiency, (int, float)) else np.nan,
            clear={YES: True, NO: False}.get(str(clear).strip() if clear is not None else "", None),
        )
    return out


def cohens_kappa(a: list, b: list) -> float:
    pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    if len(pairs) < 2:
        return np.nan
    x = np.array([p[0] for p in pairs], dtype=float)
    y = np.array([p[1] for p in pairs], dtype=float)
    po = float((x == y).mean())
    pe = float(x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean()))
    return float((po - pe) / (1 - pe)) if pe < 1 else (1.0 if po == 1 else np.nan)


def agreement(cfg: Config, paths: list, out: Path) -> Path:
    _, _, cases = load_study(cfg)
    design = {c.id: c.clarity == "clear" for c in cases}
    ratings = {Path(p).stem: read_sheet(Path(p)) for p in sorted(paths)}
    names = list(ratings)
    ids = sorted(set().union(*[set(r) for r in ratings.values()])) if ratings else []
    lines = [f"# Expert review of the study cases\n", f"Reviewers: {len(names)} ({', '.join(names) if names else 'none'}). Cases in the sheets: {len(ids)}.\n"]
    rows = ["| reviewer | rated | mean realism | mean sufficiency | agrees with the design on clarity |", "| --- | --- | --- | --- | --- |"]
    for n in names:
        r = ratings[n]
        rated = [i for i in ids if i in r and r[i]["clear"] is not None]
        agree = [r[i]["clear"] == design[i] for i in rated if i in design]
        rows.append(f"| {n} | {len(rated)} | {np.nanmean([r[i]['realism'] for i in r]) if r else float('nan'):.2f} | "
                    f"{np.nanmean([r[i]['sufficiency'] for i in r]) if r else float('nan'):.2f} | "
                    f"{(sum(agree) / len(agree)) if agree else float('nan'):.2f} ({sum(agree)} of {len(agree)}) |")
    lines.append("\n".join(rows) + "\n")
    if len(names) >= 2:
        lines.append("## Agreement between reviewers\n")
        arows = ["| measure | value |", "| --- | --- |"]
        for key, label in (("realism", "Krippendorff's alpha, realism"), ("sufficiency", "Krippendorff's alpha, sufficiency")):
            data = np.array([[ratings[n].get(i, {}).get(key, np.nan) for i in ids] for n in names], dtype=float)
            arows.append(f"| {label} | {krippendorff_interval(data):.3f} |")
        a, b = names[0], names[1]
        k = cohens_kappa([ratings[a].get(i, {}).get("clear") for i in ids], [ratings[b].get(i, {}).get("clear") for i in ids])
        arows.append(f"| Cohen's kappa, clear or ambiguous ({a} and {b}) | {k:.3f} |")
        lines.append("\n".join(arows) + "\n")
    lines.append("Agreement with the design: in a case designed as clear, the priority of the request in question should be judged to follow clearly from the facts, and in a case designed as ambiguous it should not.\n")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out
