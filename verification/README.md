# Verification records

## `adversarial-review.md`

An adversarial review written by an **AI agent** (Claude) that did not write the note. It is
**not human peer review**. The agent was told to try to refute the claim `p_min = 293`. It read
all nine upstream source files line by line (`main.tex` and the eight sections, about 6100
lines) and listed every use of `p`, `M`, `R0`, `β` and every "sufficiently large" phrase.
Its verdict was "confirmed with conditions". Each condition was then built into the note:

- More upstream lines must change than the single diameter bound at l. 592 (now Table 1).
- `R0 ≥ 2` comes from the counting argument (l. 705–708), not from the cut argument
  (now (C8) and Remark 3.3).
- The sharpened set `{199, 211}` is not upward closed (now Remark 3.3).
- The strengthened values 157/109 need a restated lemma (now Remark 3.4; no claim is made).

## `scripts/`

These are the reviewer's own scripts. They were written independently of `computations/` and
do not reuse it. They compute the centers `d_i` exactly instead of using the `p/M ± 1`
approximation.

- `indep_scan.py`: rederives every condition from the upstream text and scans for the
  minimal prime in four modes (paper or refined correction estimate; literal or exact cut
  argument).
- `diag_closure.py`: diagnoses why each prime below the threshold fails, checks upward
  closure (exact to `2·10^5`, closed form to `2·10^7`), and reproduces the upstream value
  `17,073,437` as a positive control.

```sh
cd verification/scripts && python3 indep_scan.py && python3 diag_closure.py   # slow: tens of minutes
```
