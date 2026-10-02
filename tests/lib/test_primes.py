from project_euler.lib.primes import build_spf_sieve, factor_spf


def test_factor_spf():
    spf = build_spf_sieve(300)
    assert factor_spf(245, spf) == {5: 1, 7: 2}
