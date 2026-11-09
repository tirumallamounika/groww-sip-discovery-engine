# Groww SIP — Completed 20-item AI–human comparison

**Coverage:** 20/20 human-labelled records have Gemini classification predictions (11 earlier and 9 supplied subsequently).
**Method:** Exact string agreement between supplied human labels and Gemini outputs, not independent ground-truth accuracy.

## Results

| Field | Agreement | Disagreements |
|---|---:|---:|
| Theme | **18/20 (90%)** | 2 |
| SIP status | **18/20 (90%)** | 2 |
| First-year eligibility | **18/20 (90%)** | 2 |

## All disagreements

### Theme
- **SIP004** — Human: `Other or unclear`; Gemini: `Cash-flow or competing priority`. Human rationale: The excerpt discusses expense management but does not confirm a SIP.
- **SIP008** — Human: `Market or performance uncertainty`; Gemini: `Other or unclear`. Human rationale: Fuller discussion indicates fund-performance concerns; short excerpt alone does not establish the reason.

### SIP status
- **SIP006** — Human: `Stopped`; Gemini: `Paused`. Human rationale: The user explicitly stopped SIPs due to insufficient cash.
- **SIP010** — Human: `Unknown`; Gemini: `Active`. Human rationale: SIP setup is described, but successful installments are not confirmed in the excerpt.

### First-year eligibility
- **SIP005** — Human: `No`; Gemini: `Confirmed`. Human rationale: The user reports problems attempting to start a first SIP; pre-start evidence.
- **SIP010** — Human: `Unknown`; Gemini: `Confirmed`. Human rationale: SIP setup is described, but successful installments are not confirmed in the excerpt.

## Evaluation cautions

- Human labels are self-reviewed, not independent expert consensus.
- Many public sources are marked unverifiable; source provenance limits the strength of findings.
- Exact-label agreement is not a representative estimate of real-world model accuracy.
- The 9 later predictions were obtained via a separate Gemini interaction using a constrained prompt, so this is not a single uniform benchmark run.
- For the 9 later records, the structured-output quality gate was not independently rerun.
- Some human theme labels rely on wider context than the short excerpt, potentially penalizing excerpt-only AI classification.
- The existing 3 synthetic gate failures test validation behavior, not model accuracy.

## Slide 6 wording

“20/20 golden-set excerpts classified with Gemini (11 earlier + 9 additional). Exact agreement with self-reviewed human labels: [insert figures above]. Disagreements reviewed qualitatively; source verification and independent label review remain limitations.”
