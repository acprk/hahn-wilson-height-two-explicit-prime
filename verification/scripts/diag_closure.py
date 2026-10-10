#!/usr/bin/env python3
"""(1) per-prime failure diagnosis below the thresholds; (2) upward closure: every prime >= p_min works
(full exact check up to 2e5, cheap closed-form check up to 2e7, analytic tail in REPORT.md);
(3) positive control: original op:parameters -> 17,073,437."""
from indep_scan import check, ok, is_prime
from fractions import Fraction as F
import math

def diag(p, c1mode, jmode, Rmin):
    rows = []
    for M in range(5, 41, 2):
        R0 = (M - 3) // 2
        if R0 < 1: continue
        f = check(p, M, R0, c1mode, jmode, Rmin)
        rows.append((M, R0, f))
    return rows

print('== mode A (paper C1, literal J): failures at R0=(M-3)/2 for selected primes ==')
for p in [127, 157, 167, 199, 211, 251, 283, 293]:
    print(p, [(M, R0, f) for M, R0, f in diag(p, 'paper', 'literal', 4) if M <= 17])

print('== mode D (C1v, exact J): ==')
for p in [101, 103, 107, 109]:
    print(p, [(M, R0, f) for M, R0, f in diag(p, 'C1v', 'exact', 2) if M <= 13])

def first_M(p, c1mode, jmode, Rmin):
    for M in range(5, int(math.isqrt(p)) + 2, 2):
        R0 = (M - 3) // 2
        if (2 * R0) ** 3 <= p: continue
        if ok(p, M, R0, c1mode, jmode, Rmin): return M
    return None

for tag, args, p0 in [('A', ('paper', 'literal', 4), 293), ('B', ('paper', 'exact', 2), 199),
                      ('C', ('C1v', 'literal', 4), 157), ('D', ('C1v', 'exact', 2), 109)]:
    bad = [p for p in range(p0, 200000) if is_prime(p) and first_M(p, *args) is None]
    print('closure full-exact', tag, 'primes in [%d,2e5) with no (M,R0):' % p0, bad[:10], len(bad))

# cheap closed-form version of mode A (paper text form, R0=(M-3)/2) to 2e7
def cheapA(p, M):
    R0 = (M - 3) // 2
    if R0 < 4 or M >= p: return False
    k = F(p, p - 1)
    return (F(p + 1, 2 * M) - k * (M + 1) > 1 and (2 * R0) ** 3 > p and
            (F(2 * R0 * p, M) + 3) * (p + 1) < p * p and 4 * M < p)
Ms = list(range(11, 2001, 2))
bad = []
import sys
N = 20_000_000
sieve = bytearray([1]) * (N + 1); sieve[0:2] = b'\x00\x00'
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
for p in range(293, N + 1):
    if not sieve[p]: continue
    # candidate M: smallest odd M with (M-3)^3 > p, try a few upward
    m0 = int(round(p ** (1 / 3))) + 3
    m0 -= 3; m0 += (m0 % 2 == 0)
    if not any(cheapA(p, M) for M in range(max(11, m0), m0 + 40, 2)): bad.append(p)
print('closure cheap mode A to 2e7: failures', bad[:10], len(bad))

# positive control: original parameters
def paper_orig(p, M):
    return M % 2 == 1 and M >= 81 and p > 16 * M * M and (2 * (M // 8)) ** 3 > p
best = None
for M in range(81, 3000, 2):
    lo, hi = 16 * M * M + 1, (2 * (M // 8)) ** 3
    p = lo
    while p < hi and not is_prime(p): p += 1
    if p < hi and (best is None or p < best[0]): best = (p, M)
print('positive control, original op:parameters p_min =', best)
