# Claude audit and research integration

Reviewed 14 October 2026. The initial audit and final follow-up were completed by Claude Sonnet 4.6 through the user's signed-in Claude account. Only the shareable skill, source references, and synthetic briefs were supplied. Private voice profiles and chat excerpts were excluded.

## Completed reviews

- [Initial audit](claude-initial.md): independent critique and three synthetic writing trials. It identified missing positive calibration, genre gaps, an abstract overcorrection warning, and pressure toward unsupported specificity.
- [Follow-up audit](claude-follow-up.md): review of the revised instructions and human-writing research. Claude assessed the skill as substantially sound and suggested narrower clarifications.

A longer second run attempting both a revised audit and three new drafts reached its 240-second deadline and was terminated. It produced no completed report. The completed follow-up was narrowed to instructions and research and finished within a 120-second deadline.

## Changes integrated

The skill now builds from speaker, reader, purpose, occasion, and meaningful connections in the author's material. It permits changes of organization as meaning develops, preserves effective original prose, and accommodates technical and correspondence conventions. It explicitly guards against replacing model formulas with obligatory terseness or contrived turns.

The human-writing reference adds composing-process theory, qualitative revision research, audience experiments, variation among an author's works, and controlled human/model style comparisons. It distinguishes source findings from proposed editorial practices.

Positive calibration now starts with the strongest observed author choice when evidence is sparse. Paragraph roles arise from the developing piece. Buhner's congruence test is grounded in the author's supplied emphasis and tone. Source checks examine each added factual or psychological claim; unsupported particulars are removed rather than used to fill a requested length.

## Independent assessment of Claude's suggestions

The audit was evaluated, not accepted automatically. The initial literary trial added an unsupplied mental state and explanation for the missing atlas. The argumentative trial assumed what methods the unspecified study used. The email trial assumed that two requests and a missing figure meant nobody had replied. Those claims are not established by the briefs. The audit's defense of the email inference was rejected.

The follow-up proposed preferentially weighting sentence and paragraph endings as more stable author evidence. No supplied study established that general ranking. It also proposed a fixed threshold of consecutive paragraphs for detecting overcorrection. These rules were not adopted. The final skill instead uses actual author evidence and the rhetorical function of each passage.

Its proposal that every factual claim must appear in a single source sentence was also narrowed: evidence can establish an inference through several facts. The check is support and appropriate attribution, not literal single-sentence correspondence.

The final editorial clarifications were integrated after the completed follow-up. The raw reports are preserved without rewriting their conclusions. They review instructions and synthetic tasks; they do not establish a statistical match to Riley's finished prose or exclusion from every model's style.

## Validation

The skill validator and local-reference checks passed. Installation preserves existing global instructions, is idempotent, creates an exact backup, and refuses an unrelated existing skill or an active global override. The updated installation is checked against the source files, and the shareable ZIP excludes the private profile.

## Naming

The skill was renamed Loose Thread after these audits. The unedited reports retain its earlier name, Human Imprint.
