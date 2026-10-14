# Sources and interpretation

Reviewed 14 October 2026. Editorial instructions elsewhere in this skill are original applications of these sources and user feedback. The studies do not validate this particular skill.

For human composing processes, revision, audience effects, and variation across an author's works, read [human-writing-research.md](human-writing-research.md). That reference distinguishes process theories and empirical findings from the practical questions proposed for this skill.

## Buhner

[Stephen Harrod Buhner, *Ensouling Language: On the Art of Nonfiction and the Writer's Life* (2010), publisher description and Chapter Eight excerpt](https://www.simonandschuster.ca/books/Ensouling-Language/Stephen-Harrod-Buhner/9781594773822).

The excerpt emphasizes attending to a promising observation, expressing experience concretely, comparing the words with their intended emotional meaning, and refining their sound. This skill adapts that process to supplied author material and reader experience. The full book was not available for this version; other detailed chapter methods are not represented as verified teachings. No book passages are included here.

## Model fingerprints and style drift

[Przystalski et al., *Stylometry recognizes human and LLM-generated texts in short samples*](https://arxiv.org/abs/2507.00838), journal reference: *Expert Systems with Applications* 296, 129001 (2026).

The study classifies short encyclopedic texts using linguistic features and reports greater grammatical standardization in model output. Its controlled text type limits transfer to personal essays or present model versions. It supports looking beyond conspicuous vocabulary to syntax and punctuation; it does not establish a universal detector or a writing recipe.

[Riad Maouchi, *How LLMs Transform Writing Style: A Stylometric Experiment*](https://riadmaouchi.github.io/llm-style-fingerprints/), project report with linked code and data.

Four models rewrote 80 French literary passages. Structural features were more discriminative than function-word features in this setup. Best four-way classification reached 57.5% against 25% chance. The report describes directional aggregate drift, weak per-text prompt consistency, and no human rewriting control. Treat this as a limited exploratory experiment, not a universal model identifier.

[Wang et al., *Catch Me If You Can? Not Yet: LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors*](https://arxiv.org/abs/2509.14543), EMNLP 2025 Findings.

The evaluation covers more than 400 authors and several genres. Models approximate structured styles more successfully than nuanced informal styles. This motivates genre-specific calibration and checking revisions against author samples. It does not demonstrate that a few instructions eliminate style drift.

## Installation and persistent guidance

[OpenAI, Agent Skills](https://developers.openai.com/codex/skills/) documents automatic selection, explicit invocation, and user-scoped skill discovery in `~/.agents/skills`.

[OpenAI, Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) documents global guidance in the Codex home and precedence for `AGENTS.override.md`. Global guidance makes the skill an explicit default for applicable writing tasks instead of relying solely on description matching. Other ChatGPT contexts need their own instructions or an installed skill/plugin.
