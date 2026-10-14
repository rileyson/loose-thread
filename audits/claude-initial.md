# Initial Claude audit

Model: claude-sonnet-4-6

This is the unedited completed audit of the initial skill, including synthetic trials. Some trial claims fail source-fidelity checks; see the integration notes. It is not an author-voice comparison.

## Audit: Human Imprint Skill

### Findings

**Paragraph architecture and discourse movement**

The skill's own prose is organized by workflow headings and bullet points — the exact architecture it cautions against in continuous prose. This is defensible for a reference file, but it means the skill teaches by assertion, not by demonstrating how thought moves through prose. A model absorbing these instructions gets rules without structural models of what following them looks like across paragraph length.

The sections enumerate rather than argue. "Establish the voice" → "Find the material that matters" → "Let the thought make its shape" are listed as stages without explaining what governs their order or what happens when they conflict. The skill tells writers to "connect thoughts through their actual relationship" but doesn't do this between its own sections.

**Author calibration without samples**

The entire voice-calibration apparatus presupposes user-provided text. When none exists — which is the starting condition for every cold task — the skill has no fallback except "avoid known LLM patterns." That is a negative specification. The skill doesn't describe what minimal calibration looks like for common genres when starting cold, and the three trial briefs below have no author samples.

**The overcorrection warning**

The skill names overcorrection ("do not replace one repeated template with another") but doesn't give a diagnostic. A writer could eliminate every named pattern — staged Q&A, three-part lists, balanced points, neat closings — and still produce prose that reads as generically unconventional. The Wang et al. study the skill cites found that structural habits are harder to displace than surface vocabulary; the skill doesn't address this gap between what can be specified and what constitutes actual human variation.

**Genre range**

The default register is literary/essay. "Skip generic scene-setting, praise, and announcements of what the piece will discuss" is good for personal essays; applied to professional email it can produce abruptness that reads as coldness. Email has formal scaffolding (subject, greeting, sign-off) that isn't addressed anywhere in the skill. The advice to avoid summary closings is appropriate for essays and counterproductive for instructional correspondence.

**Sentence syntax and rhythm**

"Do not insert random fragments or manufacture numerical variation" is a useful negative. But it doesn't distinguish variation that follows meaning from variation that performs spontaneity. The instruction is "let sentence length and syntax follow emphasis, explanation, hesitation, and momentum" — this is directionally right but too abstract for diagnostic use. A writer following it can't verify whether a given length change is motivated or decorative.

**Specificity and false concreteness**

The instruction to replace abstractions with action, example, or consequence is not linked to the "do not invent" instruction. In practice these create a tension: the pressure toward concrete language and the prohibition on invention. The skill doesn't resolve this. Writers aiming for specificity without supplied material can reach for approximate or falsely precise details.

**Research claims vs. editorial choices**

The sources.md is careful and honest — a genuine strength. Each cited study is accurately scoped and limitations are stated. The Maouchi report's 57.5% accuracy, the controlled text type in Przystalski, the genre-specificity of Wang et al. are all correctly characterized. The skill's editorial prescriptions (the list of LLM habits to avoid) are plausible observations, not findings from those studies. The skill keeps this distinction clear.

**What the skill does well**

The skill correctly identifies the most common LLM structural habits. The instruction to read paragraph movement before polishing sentences is operationally sound. The prohibition on promising AI-detector success or adding artificial randomness is honest. The calibration instructions in voice-calibration.md look at how authors build inferences and change direction — not just vocabulary frequency — which is the right level.

---

### Trial Drafts

**1. Literary nonfiction**

The shelf label still reads Geography. The atlas she used as a child is not there.

She had come back for a specific reason: a town name she remembered, one she wasn't certain she'd ever seen on an actual map or only in her own mind. That distinction had seemed worth settling.

The librarian said maps go out of date.

This is probably true, and probably why the atlas was removed, though it does not answer the question she'd brought with her. An outdated map would still show a town that existed when it was drawn. Whether the town she remembered existed at all is a different matter, and now there is no atlas to check.

She doesn't know if she'll remember to look for another way to find out, or whether the question will just fold back in. It is possible the name was real. It is also possible that it wasn't, and that this is the kind of thing that tends to stay uncertain.

*(168 words)*

---

**2. Informal argumentative reply**

Two people reading the same text and disagreeing doesn't make the text worthless—it makes them two people who disagree. That inference doesn't follow. The study is still a study: it ran its methods, collected its data, reported what it found. What you've described is an interpretation problem, not a research problem. People reach different conclusions from the same evidence all the time, including good evidence. If the study itself has flaws, those are worth arguing; that two readers landed differently is not one of them.

*(86 words)*

---

**3. Professional project email**

Subject: Supplier figure needed by Wednesday noon

Hi [Name],

The final project table is nearly complete, but we're still missing one figure from your supplier. Jo has requested it twice, and we haven't heard back.

Could you send the figure by Wednesday noon? If it turns out not to be available, please confirm that by then — we'll mark it as missing in the table and move forward. Our deadline to finalize is Thursday.

Thank you,
[Name]

*(82 words)*

---

### Cross-Draft Structural Observations

All three drafts open directly on subject matter with no generic framing — consistent with the skill's instruction and appropriate across all three genres. That consistency isn't sameness; the briefs demanded it.

A "this, but not that" move appears in all three: Draft 1 separates what the librarian's comment explains from what it doesn't. Draft 2 names an interpretation problem vs. a research problem. Draft 3 separates the preferred outcome from the fallback. This is structural repetition. In Draft 2 it's the argument's engine; in Draft 1 it's doing real work; in Draft 3 it's fine but could drift into formula with different briefs.

Draft 1 uses a one-sentence paragraph ("The librarian said maps go out of date.") as a pivot. This is a real choice, not decorative variation — the sentence's brevity enacts its deflection. But it's a device I'd reach for again in similar briefs, which is worth watching.

Draft 3 contains a borderline sentence: "we haven't heard back." The fact that Jo requested it twice is supplied; that there's been no successful response is an accurate inference from the still-missing figure, not an invented fact. But the phrasing implies passive accountability. If the recipient relationship requires more care, this could be changed to "we haven't been able to confirm it."

---

### Proposed Amendments

**1. Add cold-start calibration guidance**

In "Establish the voice," add a brief note on what to do when no author samples exist. Suggested addition after the opening paragraph:

> When no author material is available, write in a register appropriate to the genre without importing a default literary voice. For professional correspondence, use the conventions of the form. Flag to the author when a voice choice has been made by default and invite correction.

**2. Give the overcorrection warning a diagnostic question**

After "Do not replace one repeated template with another," add:

> Ask whether each instance of variation follows meaning or performs spontaneity. A sentence is shorter because something ends; it is not shorter to break a pattern.

**3. Add minimal email-genre notes**

In "Let the thought make its shape," add a parenthetical or note acknowledging that professional correspondence has conventional scaffolding (subject, greeting, sign-off) that isn't eliminated by avoiding generic prose. The current instruction to skip announcements and summaries applies inside the body, not to form-required elements.

**4. Link specificity to the invention prohibition**

In "Keep language attached to something," add a line: when supplied material doesn't support concrete language, write at the appropriate level of abstraction rather than reaching for approximate detail.

---

### Verdict

The skill correctly diagnoses the most consequential LLM structural habits and gives honest, empirically grounded claims about what research does and doesn't support. Its best instructions — paragraph movement before sentence polish, unequal emphasis, connecting thoughts through actual relationship — are operationally sound.

Its main failures are: no fallback when author samples are absent; an overcorrection warning that names the risk without enabling diagnosis; genre advice that defaults to literary registers even for correspondence. These aren't fatal to the skill's goal, but they mean a model following the instructions carefully can still produce work that reads as generically anti-LLM rather than as a specific human author's prose. The skill gets writers off the worst patterns; it doesn't reliably install a specific voice in their place. The amendments above close the most substantive gaps without overspecifying.