# Claude follow-up audit

Model: claude-sonnet-4-6

This is the unedited completed review of the revised candidate and research. See the integration notes for the changes adopted or rejected afterward.

## Audit Report: human-imprint skill

**Overall verdict:** The skill is substantially sound. The research citations are handled with appropriate hedging, the Buhner attribution is appropriately scoped, and the anti-overcorrection logic is unusually explicit. The defects below are real but mostly narrow.

---

### 1. Positive author calibration — partially underdeveloped

**Location:** SKILL.md, "Establish the voice," paragraphs 3–4; voice-calibration.md, "Notice decisions, not just word counts."

**Defect:** The skill says what *not* to do with thin evidence (don't claim a verified match, don't invent exemplars) but gives less concrete guidance on what *to do*. When a user has only two paragraphs of prose, the assistant needs a positive fallback: which features of those paragraphs are most load-bearing (openings, how conclusions arrive, syntactic rhythm at emphasis points)?

**Correction:** In voice-calibration.md, add a sentence under "Notice decisions, not just word counts": *When samples are sparse, weight the author's sentence-closing moves and paragraph-ending decisions most heavily — these are more individually stable than mid-sentence syntax and easier to preserve from limited evidence.*

---

### 2. Genre adaptability — the list in "Let the thought make its shape" skews toward essay/nonfiction

**Location:** SKILL.md, "Let the thought make its shape," bullet list.

**Defect:** Most bullets assume discursive prose. The guidance on headings, bullets, and tables is a single permissive sentence. For instructional, technical, or correspondence genres, the affirmative case for structured form is underweighted compared to the discouragement of unnecessary outlining.

**Correction:** Split the headings/bullets bullet into two: one permissive sentence for navigation-heavy genres, and a second explicitly noting that in correspondence and technical writing, imposed continuity can obscure rather than express the author's structure.

---

### 3. Thought and paragraph development — "reason to exist" criterion is underspecified

**Location:** SKILL.md, "Let the thought make its shape," second bullet.

**Defect:** "Make a claim, examine evidence, notice a detail, turn the thought, or let something land" is a list of valid functions but reads as parallel options rather than a hierarchy. In an argument, some of these (noticing a detail, letting something land) may be structurally subordinate to the claim/evidence pair. A draft that assigns each paragraph one function from this list could still be mechanically uniform.

**Correction:** Add: *A paragraph's function should follow from its position in the developing argument, not from rotation through these options.*

---

### 4. Overcorrection into a new model house style — addressed but incompletely enforced

**Location:** SKILL.md, "Revise the structure, then the surface," final two paragraphs; revision-checks.md, "Cadence."

**Defect:** The skill correctly warns against trading one template for another, but the self-test it proposes ("compare a batch of related drafts for a repeated new house style") requires multiple drafts. For a single piece, the check is underdeveloped. The revision-checks.md note on "spare declaratives, one-line pivots" identifies the most common overcorrection patterns but does not tell the assistant how to interrupt them mid-draft.

**Correction:** In revision-checks.md under "Cadence," add: *Within a single draft, if more than two consecutive paragraphs end with a one-sentence conclusion or begin with a short declarative, treat that as a candidate overcorrection regardless of whether other drafts are available for comparison.*

---

### 5. Buhner calibration — "emotional meaning" language not reconciled with the skill's own warnings

**Location:** sources.md, Buhner section; SKILL.md, "Find the material that matters."

**Defect:** sources.md accurately summarizes the excerpt as including "comparing the words with their intended emotional meaning." SKILL.md says "Do not pretend to experience the author's feelings or a writing trance" — correct. But the skill never resolves how to apply Buhner's *congruence* test (does the language match what the experience should convey?) without access to the author's experiential intent. The practical instruction is absent.

**Correction:** In "Find the material that matters," add: *Apply Buhner's congruence test from the supplied material outward — ask whether the draft's language matches the weight and texture the author's own words assign to the experience, not an imagined emotional state.*

---

### 6. Factual fidelity — "length target does not authorize invention" is stated twice

**Location:** SKILL.md, "Keep language attached to something" and "Revise the structure, then the surface"; revision-checks.md, "Intent and truth."

**Defect:** Not a logical error, but the repetition without escalation means neither instance carries full weight. One should be the rule; the other should supply the operational test (how to detect the violation).

**Correction:** In SKILL.md retain the rule; in revision-checks.md, make it the test: *For each claim added during revision, locate the source sentence that establishes it. If none exists, the claim was invented.*

---

### Minor: research/application boundary

The human-writing-research.md file consistently marks applications as "editorial applications to evaluate." This is accurate and appropriate. No correction needed.

---

**Summary of required changes:** Six locations. Two add a sentence (voice-calibration.md, revision-checks.md cadence), two restructure a bullet or add a clarifying sentence (SKILL.md paragraph functions, genre adaptability), one resolves a cross-reference gap (Buhner congruence test), one consolidates a repeated instruction (factual fidelity). None requires structural revision of the skill.