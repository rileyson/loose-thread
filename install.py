#!/usr/bin/env python3
"""Install the bundled skill and optionally set a global writing default."""
import argparse
import hashlib
from pathlib import Path
import shutil
import time

BEGIN = "<!-- human-imprint:begin -->"
END = "<!-- human-imprint:end -->"
MAX_FILES = 32
MAX_BYTES = 512_000


def inventory(root):
    started = time.monotonic()
    files = {}
    total = 0
    for path in root.rglob("*"):
        if time.monotonic() - started > 10:
            raise ValueError("Skill inventory exceeded its 10-second deadline.")
        if path.is_symlink():
            raise ValueError(f"Unexpected symlink: {path}")
        if len(path.relative_to(root).parts) > 4:
            raise ValueError("Skill directory exceeds the supported depth.")
        if path.is_file():
            total += path.stat().st_size
            if len(files) >= MAX_FILES or total > MAX_BYTES:
                raise ValueError("Skill exceeds the bounded file or byte limit.")
            files[path.relative_to(root)] = path.read_bytes()
    return files


def instruction_block(skill, profile):
    profile_line = (
        f"For the author's voice preferences, read `{profile}` when this skill applies. "
        "Keep that profile private; update it only within the user's authorization.\n"
        if profile else ""
    )
    return (
        f"{BEGIN}\n"
        "## Writing together\n\n"
        f"For prose drafting, rewriting, editing, and sustained writing collaboration, "
        f"read and apply the human-imprint skill at `{skill / 'SKILL.md'}` by default. "
        "Use available author samples and corrections, adapt to genre, and preserve "
        "the author's intent and factual material. Review structure and cadence as "
        "well as wording. For brief routine replies, use plain direct language "
        "without canned framing or redundant summaries. "
        "Current user instructions and project requirements take priority.\n"
        f"{profile_line}{END}"
    )


def install(args):
    source = Path(__file__).resolve().parent / "skills" / "human-imprint"
    files = inventory(source)
    if Path("SKILL.md") not in files:
        raise ValueError("Bundled SKILL.md is missing.")
    target = args.skills_dir.expanduser().absolute() / "human-imprint"
    codex_home = args.codex_home.expanduser().absolute()
    profile = args.profile.expanduser().resolve() if args.profile else None
    if profile and not profile.is_file():
        raise ValueError(f"Voice profile does not exist: {profile}")
    if target.is_symlink():
        raise ValueError(f"Existing skill is a symlink; inspect it before changing: {target}")
    if target.exists() and (not target.is_dir() or inventory(target) != files):
        raise ValueError(f"A different skill already exists at {target}; no files changed.")

    guidance = codex_home / "AGENTS.md"
    previous = b""
    updated = None
    if args.global_default:
        override = codex_home / "AGENTS.override.md"
        if override.exists() and override.read_text().strip():
            raise ValueError(f"Global override is active at {override}; no files changed.")
        if guidance.is_symlink():
            raise ValueError(f"Global instructions are a symlink: {guidance}")
        previous = guidance.read_bytes() if guidance.exists() else b""
        if len(previous) > 128_000:
            raise ValueError("Global instructions exceed the installer byte limit.")
        text = previous.decode("utf-8")
        block = instruction_block(target, profile)
        if BEGIN in text or END in text:
            if text.count(BEGIN) != 1 or text.count(END) != 1:
                raise ValueError("Ambiguous existing writing section; no files changed.")
            start = text.index(BEGIN)
            finish = text.index(END) + len(END)
            if finish < start:
                raise ValueError("Malformed writing section; no files changed.")
            text = text[:start] + block + text[finish:]
        else:
            text = text + ("\n\n" if text else "") + block + "\n"
        updated = text.encode("utf-8")

    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)
    if updated is not None and updated != previous:
        codex_home.mkdir(parents=True, exist_ok=True)
        if previous:
            digest = hashlib.sha256(previous).hexdigest()[:12]
            backup = codex_home / f"AGENTS.md.human-imprint-backup-{digest}"
            if not backup.exists():
                with backup.open("xb") as stream:
                    stream.write(previous)
            elif backup.read_bytes() != previous:
                raise ValueError("Instruction backup collision; global instructions unchanged.")
        # Refuse to overwrite another task's intervening edit.
        current = guidance.read_bytes() if guidance.exists() else b""
        if current != previous:
            raise ValueError("Global instructions changed during installation; retry after reviewing.")
        guidance.write_bytes(updated)
    if inventory(target) != files:
        raise ValueError("Installed skill verification failed.")
    if updated is not None and guidance.read_bytes() != updated:
        raise ValueError("Global instructions verification failed.")
    print(f"Verified skill: {target}")
    if args.global_default:
        print(f"Verified global writing default: {guidance}")
    if profile:
        print(f"Private profile referenced: {profile}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-default", action="store_true")
    parser.add_argument("--profile", type=Path)
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    try:
        install(parser.parse_args())
    except (ValueError, OSError, UnicodeError) as error:
        parser.exit(1, f"Install stopped: {error}\n")
