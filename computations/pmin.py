#!/usr/bin/env python3
"""Explicit prime range for the OpenAI height-two Hahn-Wilson counterexamples.

Every numerical condition that Section `op` (operator.tex) of the upstream
preprint imposes on (p, M, R0) is checked in exact rational arithmetic, after
replacing R0 = floor(M/8) by a free parameter R0 <= (M-3)/2 and the diameter
bound p/4+3 by 2*R0*p/M+3 (see paper/main.tex, Table 1 for the line map).

Usage: python3 pmin.py            (all checks, a few seconds)
"""
from fractions import Fraction as F
import math, sys


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def failures(p, M, R0, Rmin=4):
    """Return the list of violated conditions (empty list = admissible)."""
    bad = []
    if M % 2 == 0 or M < 3:
        return ['M odd']
    s0 = (M - 1) // 2
    q = p + 1
    kappa = F(p, p - 1)                                   # (op:kappa)
    # (N0) global prime hypotheses of the other sections
    if p <= 8:
        bad.append('p>8')
    # (C1) op:correction-bound with b >= X/(2M), r'_m <= kappa*m < kappa*(M+1)X
    if not F(q, 2 * M) - kappa * (M + 1) > 1:
        bad.append('C1')
    # (Cbeta) beta = log_p(2 R0) > 1/3
    if not (2 * R0) ** 3 > p:
        bad.append('beta')
    # (CR) R0 large enough for the cut argument ("within three places of s0")
    if R0 < Rmin:
        bad.append('R0>=%d' % Rmin)
    # (CI) I = {s0-R0+1..s0+R0} meets neither endpoint 0, M-1
    if not (s0 - R0 + 1 >= 1 and s0 + R0 <= M - 2):
        bad.append('I interior')
    # (CM) M < p (polynomials of degree <= M < p in one digit)
    if not M < p:
        bad.append('M<p')
    # (CS) same-cluster lower-portion difference D*X/p^2 below X/q
    D = F(2 * R0 * p, M) + 3
    if not D * q < p * p:
        bad.append('CS')
    # (CB) first band: deviation 1/p + D/p^2 <= 2/p, separated from k1=2,
    #      and lower end >= X/(2M)
    if not F(1, p) + D / p ** 2 <= F(2, p):
        bad.append('band dev')
    if not F(1, M) + F(2, p) < F(2, M) - F(2, p):
        bad.append('band sep')
    if not F(1, M) - F(2, p) >= F(1, 2 * M):
        bad.append('band low')
    # (C0) base stage d = floor(p/M): q d < p^2, d >= p/(2M), d <= delta
    d = p // M
    if not (q * d < p * p and 2 * M * d >= p and d <= (p - 1) // 2 and d >= 1):
        bad.append('base')
    # (Cc) centers d_i distinct, d_{s0} = delta
    cent = [(2 * i + 1) * p // (2 * M) for i in range(M)]
    if len(set(cent)) < M or cent[s0] != (p - 1) // 2:
        bad.append('centers')
    return bad


def witnesses(p, Rmin=4):
    out = []
    for M in range(3, min(p, 4 * math.isqrt(p) + 50), 2):
        for R0 in range(1, (M - 3) // 2 + 1):
            if not failures(p, M, R0, Rmin):
                out.append((M, R0))
    return out


def main():
    ok = True
    print('== 1. smallest admissible prime (R0 >= 4, the paper\'s cut argument verbatim)')
    pmin = next(p for p in range(3, 10 ** 4) if is_prime(p) and witnesses(p))
    print('   p_min =', pmin, ' witnesses (M,R0):', witnesses(pmin)[:4])
    ok &= pmin == 293 and (11, 4) in witnesses(293)
    print('   margins at (p,M,R0)=(293,11,4): C1 =',
          F(294, 22) - F(293, 292) * 12 - 1, ', (2R0)^3 - p =', 8 ** 3 - 293)

    print('== 2. why every prime below 293 fails (M = 11 is the only M that can work)')
    for p in [q for q in range(11, 293) if is_prime(q)]:
        for M in range(3, p, 2):
            for R0 in range(1, max(1, (M - 3) // 2) + 1):
                f = failures(p, M, R0)
                if not f:
                    ok = False
                    print('   UNEXPECTED witness', p, M, R0)
    # diagnostic: C1 alone forces p >= 293 at M = 11 and more for M >= 13
    for M in (11, 13, 15):
        t = next(p for p in range(11, 10 ** 5) if is_prime(p) and 'C1' not in failures(p, M, 4))
        print('   M=%d: first prime satisfying C1 = %d' % (M, t))
    print('   M<=9 forces R0<=3 (needs R0>=4); M>=11 needs C1 => p>=293')

    print('== 3. upward closure: exact check of every prime in [293, 1000)')
    bad = [p for p in range(293, 1000) if is_prime(p) and not witnesses(p)]
    print('   primes without witness:', bad)
    ok &= not bad
    print('   (p >= 1000 is Lemma 3.2 of the note; spot check below)')
    for p in [1009, 10007, 10 ** 6 + 3, 10 ** 9 + 7, 10 ** 12 + 39]:
        e = 2
        while e ** 3 <= p:
            e += 2
        M = e + 3
        if p < 10 ** 7:
            f = failures(p, M, (M - 3) // 2)
        else:   # closed-form conditions of Lemma 3.2 (avoids listing 10^4 centers)
            kappa = F(p, p - 1)
            f = [] if (F(p + 1, 2 * M) - kappa * (M + 1) > 1 and (M - 3) ** 3 > p
                       and 4 * M < p) else ['closed form']
        print('   p=%d M=%d R0=%d ->' % (p, M, (M - 3) // 2), 'ok' if not f else f)
        ok &= not f

    print('== 4. variant: sharpened cut argument (R0 >= 2), Remark 3.4')
    S = [p for p in range(11, 1000) if is_prime(p) and witnesses(p, Rmin=2)]
    print('   admissible primes < 1000 start:', S[:4], '... gap:',
          [p for p in range(S[0], 293) if is_prime(p) and p not in S])
    ok &= S[:2] == [199, 211] and all(p in S for p in range(293, 1000) if is_prime(p))

    print('== 5. positive control: original (op:parameters) M>=81, p>16M^2, 2floor(M/8)>p^(1/3)')
    best = None
    for M in range(81, 3001, 2):
        lo, hi = 16 * M * M + 1, (2 * (M // 8)) ** 3
        p = lo
        while p < hi and not is_prime(p):
            p += 1
        if p < hi and (best is None or p < best[0]):
            best = (p, M)
    print('   original p_min =', best, ' ratio = %.0f' % (best[0] / 293))
    ok &= best[0] == 17073437
    print('ALL CHECKS PASSED' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
