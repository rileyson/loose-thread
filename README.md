# Human Imprint

A writing skill for prose that follows an author's material, voice, and movement of thought. It helps draft and edit nonfiction, essays, bios, correspondence, and other prose while checking the recurring structures that can make model output sound canned.

The skill combines an original adaptation of the published excerpt from Stephen Harrod Buhner's *Ensouling Language* with research on model style drift and author calibration. Attribution and evidence limits are in [sources.md](skills/human-imprint/references/sources.md). It contains no book excerpts or private writing samples.

[Human writing research](skills/human-imprint/references/human-writing-research.md) explains the research on composing, revision, context, and author variation, and how the skill applies it. The skill supports a range of human forms rather than equating human voice with minimalism.

[Claude audit and integration notes](audits/integration.md) preserve the independent reviews, synthetic trial failures, and the decisions made when revising the skill.

## Install

Download this repository as a ZIP using GitHub's **Code → Download ZIP**, unzip it, and run from its directory:

```sh
python3 install.py --global-default
```

The installer copies the skill to `~/.agents/skills/human-imprint` and adds a small marked section to the global Codex `AGENTS.md`. It preserves existing instructions and backs up that file before changing it. Without `--global-default`, installation only makes the skill available for automatic selection or explicit invocation.

You can keep your own voice profile outside the repository:

```sh
python3 install.py --global-default --profile /absolute/path/to/voice-profile.md
```

The installer points to that file; it does not upload or copy the profile into this repository. Customize `--skills-dir` and `--codex-home` for another local profile. It stops rather than overwriting a different existing skill or adding guidance hidden by a nonempty global override.

## Use

Ask for writing or editing normally when installed as a global default. You can also explicitly invoke it:

```text
Use $human-imprint to revise this essay. Keep my argument and voice.
```

Codex detects installed skill changes automatically; start a new session if it does not appear. Global instructions are read at session startup. Installation on one Mac does not change instructions in separate ChatGPT chats or on other hosts. For those contexts, use [chat-instructions.txt](chat-instructions.txt) in their custom or project instructions, or install the skill through the host's supported skill/plugin mechanism.

## Personalization

The skill uses relevant author samples and corrections already available in the current context. A private profile can preserve confirmed preferences between tasks. It distinguishes conversational feedback from finished prose and adapts to genre; it does not treat a user's angriest message as the voice of their entire body of work.

Its quality should be judged through actual revisions and author feedback. It makes no detector-passing or fingerprint-removal claim.

## Remove the default

Remove only the section between `<!-- human-imprint:begin -->` and `<!-- human-imprint:end -->` from the global `AGENTS.md`. Remove the installed `human-imprint` folder if you also want to remove the skill. Leave other instructions and private profiles intact.
