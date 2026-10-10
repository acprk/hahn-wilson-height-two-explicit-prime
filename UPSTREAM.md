# Upstream provenance

This repository contains no code or text copied from other repositories. It analyses one
preprint in [OpenAI's mathematics repository](https://github.com/openai/math), at commit
[`08fcd618213aa43b0fcaff4526a8a48d66d02e55`](https://github.com/openai/math/tree/08fcd618213aa43b0fcaff4526a8a48d66d02e55/preprints):

- *Counterexamples to the Hahn–Wilson conjecture at height two* (OpenAI, September 26, 2026),
  directory
  `preprints/Counterexamples-to-the-Hahn-Wilson-conjecture-at-height-two-September-26-2026`.

That preprint proves the result for every sufficiently large prime `p`. All of the mathematics
is in it. This repository only makes the prime range explicit (`p ≥ 293`), by choosing one
parameter differently in its Section `op` (`build/sections/operator.tex`). Line numbers quoted
here refer to that file at the commit above.
