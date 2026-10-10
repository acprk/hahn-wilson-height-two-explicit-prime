# Adversarial review: `p_min = 293` (AI agent, 2026-10-09)

**Reviewer:** an AI agent (Claude) that did not write the note, instructed to refute the claim
first and to confirm it only if refutation failed. This is not human peer review.

**Verdict: CONFIRMED, with conditions** (all conditions are now built into the note).

## 1. Full reading of the upstream source (about 6100 lines, nine files)

- Only two conditions actually constrain `p`:
  - **C1**, the correction bound (operator.tex l. 322–327);
  - **β > 1/3**, i.e. `(2R0)^3 > p` (l. 503).
- Global hypotheses elsewhere are all satisfied for `p ≥ 127`:
  - geometry needs `p > 5` (l. 14), `p > 3` (l. 629) and weight `≥ p > 4` (l. 702);
  - completion and gluing need `D > 2` or `D > 3`;
  - comparison and transfer need `p > 8` and `D > 12`, and the sparse lemma needs `D > 7`;
  - `2p − 2 > n² + n` (consequences l. 430) appears only in a remark.
- Every other operator-internal condition was checked at `p = 293` using exact centers:
  - `M < p`;
  - distinct centers and `d_{s0} = δ`;
  - the base stage `d = 26`;
  - same-cluster difference `< X/q`;
  - the first band: inside the stage, separated from `k1 = 2`, no wrap, lower end `≥ X/(2M)`;
  - the cut argument.
- The `1/3` in `O(N^{1/3})` (obstruction section) comes from `N_{p^s} ≥ p^{3(s−1)}` and does
  not depend on `p`. Its constant depends on `p`, which is harmless.
- All occurrences of "sufficiently large d / N / X / stage" (operator l. 140, 513, 680, 719;
  gluing l. 192, 224; obstruction l. 1069) refer to `N`, stages or torsion level, not to `p`.
  No implicit "p large, hence negligible / zero / convergent / non-overlapping" argument was
  found.

## 2. Independent recomputation (`scripts/`)

| Mode | Result |
| --- | --- |
| Positive control: original conditions | 17,073,437 (`M = 1033`) |
| Drop `M ≥ 81` and `p > 16M²`, keep `R0 = ⌊M/8⌋` | 38,113 (`M = 137`) |
| Paper C1, literal cut argument (`R0 ≥ 4`), `R0 ≤ (M−3)/2` | **293**, `(M, R0) = (11, 4)` |
| Paper C1, `R0 ≥ 2` | 199 and 211, then 14 failures (223–283), then all `p ≥ 293` |
| Refined C1 (exact band depth), `R0 ≥ 4` | 157 (not proved; needs a restated lemma) |
| Refined C1, `R0 ≥ 2` | 109, `(M, R0) = (9, 3)` (not proved) |

- At `p = 293` the C1 margin is `0.3225`, and `(2R0)^3 = 512 > 293`.
- Below 293: with `M ≥ 11`, every prime fails only C1; with `M ≤ 9`, it fails `R0 < 4` or
  β > 1/3.
- Upward closure for the main mode: no failure in `[293, 2·10^5)` (exact) or `[293, 2·10^7]`
  (closed form). The note replaces this with a hand proof (Lemmas 3.1–3.2).

## 3. Corrections to the first internal write-up

- `R0 ≥ 2` comes from l. 705–708: `d(I)` needs a digit below `δ`, and `d(I−1)` a digit above
  `δ`. Exactly computed, the cut argument only meets `i ∈ {s0, s0+1}`.
- "199" is not upward closed.
- The strengthened values are 157/109, not 167/127 as first reported.
- The single change at l. 592 is not sufficient. The full list of changes is Table 1 of the
  note.

## 4. Prior work

A web search found no explicit prime bound for this construction. All public descriptions
say "sufficiently large p".

## 5. Character of the result

This is a parameter re-tuning. The original argument is unchanged, and the loss came entirely
from slack parameters chosen for readability (`M ≥ 81`, `p > 16M²`, `R0 = ⌊M/8⌋`). No step of
the original method fails.
