# An explicit prime range for the height-two Hahn–Wilson counterexamples

OpenAI's preprint *Counterexamples to the Hahn–Wilson conjecture at height two*
(September 26, 2026) constructs, **for every sufficiently large prime `p`**, a connective
`p`-complete spectrum of exact fp-type two outside `Thick(BP⟨2⟩_p^∧)`. The preprint gives no
numerical range. Its parameter conditions first hold at `p = 17,073,437`.

This repository contains a short note and the computations behind it. They show that, **with
one parameter chosen differently and the argument otherwise unchanged, the construction works
for every prime `p ≥ 293`**. They also show that 293 is the least prime this argument can
reach.

The results were found and checked by **Claude (Anthropic) agents** working under the
direction of the repository owner, [AUTHOR NAME]. **This is a re-tuning of constants, not new
mathematics.** It is conditional on the correctness of the upstream preprint. No human peer
review has taken place, and nothing here is formalized in Lean. See
[Status and caveats](#status-and-caveats).

**Note:** [*An explicit prime range for the height-two counterexamples to the Hahn–Wilson
conjecture*](paper/main.pdf) ([LaTeX source](paper/main.tex), [build
instructions](paper/README.md)).

## What is proved

| Prime range | Statement | Kind of proof |
| --- | --- | --- |
| `p ≥ 17,073,437` | Upstream conditions `M ≥ 81`, `p > 16M²`, `2⌊M/8⌋ > p^{1/3}` (first prime, `M = 1033`) | upstream |
| **`p ≥ 293`** | Upstream Theorem 1.1 holds, after the eight line-level changes in Table 1 (**Theorem A**) | note, by hand; checked by computer |
| `p < 293` | Not reachable by this argument with every estimate as written (**Theorem B**) | note, by hand; checked by computer |
| `p ∈ {199, 211}` | Also reached by a sharper reading of the cut argument; 223–283 are still not reached (**Remark 3.3**) | note |
| 157 / 109 | Where a refined correction estimate would lead; **not claimed** (Remark 3.4) | computation only |

The improvement factor is about `5.8 × 10^4`.

### Where the constant was lost

The "sufficiently large" hypothesis enters through a single proposition, the operator with
persistent defects (upstream Section `op`). Every other section needs only `p > 8` or
`p > 5`. Inside Section `op`, only two estimates really constrain `p`:

- **C1**, the correction bound for the coefficient-control lemma:
  `(p+1)/(2M) − p(M+1)/(p−1) > 1`;
- **β > 1/3**, the growth exponent: `(2R0)^3 > p`.

The upstream text takes `R0 = ⌊M/8⌋`, which forces `M ≳ 4p^{1/3}`. C1 then forces
`p ≳ 2M²`, and this is where the 17-million bound comes from. `R0` is only used in two
places:

- a diameter bound at l. 592, `p/4 + 3`, which becomes `2R0·p/M + 3`;
- the cut argument at l. 694, which needs `R0 ≥ 4`.

So `R0 = (M−3)/2` is allowed. The criterion becomes: some odd `M ≥ 11` satisfies C1 and
`(M−3)^3 > p`. At `M = 11` this first happens at `p = 293`. Below 293, C1 is the estimate
that fails.

## Repository layout

- `paper/`: LaTeX source, bibliography and PDF of the note (4 pages).
- `computations/pmin.py`: checks every condition (C0)–(C8) in exact rational arithmetic, for
  each prime and each `(M, R0)`. It confirms:
  - the minimum 293;
  - that no prime below 293 works;
  - every prime in `[293, 1000)`, plus spot checks up to `10^12`;
  - the `{199, 211}` variant;
  - the upstream value 17,073,437 as a positive control.

  `computations/run_all.sh` runs it (about 40 s, Python 3 only).
- `verification/`: an adversarial review by an AI agent, and that reviewer's independent
  scripts.

## Status and caveats

- **Not new mathematics.** The note changes no idea of the upstream proof. It only chooses
  one parameter differently and rewrites one estimate. An expert could do this in an
  afternoon. We record it because the upstream statement gives no explicit range.
- **Conditional on upstream.** We have not independently verified the upstream preprint
  beyond the numerical steps of its operator section. If the upstream proof has a gap, so
  does Theorem A.
- **No human peer review.** The review in [`verification/`](verification/) was written by an
  AI agent and is not peer review.
- **Not formalized.** Only the finite numerical conditions are machine-checked.
- **No historical-priority claim.** "Explicit" means "not found in the literature we were
  able to read". A web search found no published explicit range.

## AI attribution

The results in this repository were found, verified and written up by Claude (Anthropic)
agents working under the direction of the repository owner, [AUTHOR NAME]. This covers the
analysis, the note and the computations. The review was also produced by an AI agent. The
human owner directed the work and is responsible for its release.

## Citation

See [`CITATION.cff`](CITATION.cff). Please also cite the OpenAI preprint listed in
[`UPSTREAM.md`](UPSTREAM.md).
