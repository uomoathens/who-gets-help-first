from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .analyze import analyze
from .attributes import Attributes
from .cases import CaseError, load_cases
from .config import load_config
from .expand import expand
from .prompts import Prompts, build
from .run import execute, jobs, load_study


def cmd_check(args) -> int:
    cfg = load_config(args.config)
    attributes, prompts, cases = load_study(cfg)
    n = sum(1 for _ in jobs(cfg, cases, attributes, prompts))
    print(f"{len(cases)} cases, {sum(len(expand(c, attributes)) for c in cases)} variants, {n} prompts across {len(cfg.models)} model(s)")
    return 0


def cmd_preview(args) -> int:
    cfg = load_config(args.config)
    attributes = Attributes.load(cfg.attributes)
    attributes.check()
    prompts = Prompts.load(cfg.prompts)
    cases = [c for c in load_cases(cfg.cases) if args.case in (None, c.id)]
    if not cases:
        raise CaseError(f"no case {args.case!r}")
    parts = []
    for case in cases:
        for variant in expand(case, attributes):
            if args.variant and variant.key != args.variant:
                continue
            for lang in args.lang or cfg.languages:
                p = build(case, variant, lang, args.paraphrase, args.role or prompts.roles()[0], 0, attributes, prompts)
                parts.append(f"## {case.id} · {variant.key} · {lang}\n\n**System:** {p.messages[0]['content']}\n\n" + p.messages[1]["content"] + "\n")
    text = "\n".join(parts)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(text)
    return 0


def cmd_run(args) -> int:
    execute(load_config(args.config), limit=args.limit, only_model=args.model)
    return 0


def cmd_analyze(args) -> int:
    analyze(load_config(args.config))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="whf", description="Who Gets Help First? Counterfactual audit of LLM decisions in flood response.")
    sub = ap.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check", help="validate cases, names and prompts and count the prompts")
    c.add_argument("--config", required=True)
    c.set_defaults(func=cmd_check)
    pv = sub.add_parser("preview", help="render prompts for reading")
    pv.add_argument("--config", required=True)
    pv.add_argument("--case")
    pv.add_argument("--variant")
    pv.add_argument("--lang", action="append", choices=["el", "fr", "en"])
    pv.add_argument("--paraphrase", type=int, default=0)
    pv.add_argument("--role")
    pv.add_argument("--out")
    pv.set_defaults(func=cmd_preview)
    r = sub.add_parser("run", help="send every prompt to every model and store the answers")
    r.add_argument("--config", required=True)
    r.add_argument("--limit", type=int)
    r.add_argument("--model")
    r.set_defaults(func=cmd_run)
    a = sub.add_parser("analyze", help="compute the pre-registered measures")
    a.add_argument("--config", required=True)
    a.set_defaults(func=cmd_analyze)
    args = ap.parse_args(argv)
    try:
        return args.func(args)
    except CaseError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
