import pytest
from fractions import Fraction
from reference.codec import (offset_decode, signed_decode, recode_nibble,
                             recode_bytes, pack, unpack)


def test_all_nibbles_and_rational_scales():
    scales = [Fraction(1, 2**24), Fraction(1, 8), Fraction(3, 2), Fraction(65504)]
    assert len({recode_nibble(c) for c in range(16)}) == 16
    for c in range(16):
        assert recode_nibble(recode_nibble(c)) == c
        assert signed_decode(recode_nibble(c)) == offset_decode(c)
        for s in scales:
            assert s * signed_decode(recode_nibble(c)) == s * offset_decode(c)


def test_all_256_byte_states_and_both_inverse_directions():
    assert len(set(recode_bytes(bytes(range(256))))) == 256
    for b in range(256):
        raw = bytes([b]); mapped = recode_bytes(raw)
        assert unpack(raw) == unpack(mapped, signed=True)
        assert recode_bytes(mapped) == raw
        assert pack(unpack(raw)) == raw
        assert pack(unpack(raw), signed=True) == mapped


def test_negative_eight_is_preserved_not_clipped():
    assert unpack(pack([-8, 7])) == (-8, 7)
    assert unpack(pack([-8, 7], signed=True), signed=True) == (-8, 7)
    # Negation is not closed on all signed INT4 states: -(-8)=8 is inadmissible.
    with pytest.raises(ValueError): pack([8, 0])


@pytest.mark.parametrize('x', [-1, 16, .5, True])
def test_invalid_nibbles(x):
    with pytest.raises(ValueError): recode_nibble(x)


def test_empty_and_invalid_packing():
    assert pack([]) == b'' and unpack(b'') == ()
    with pytest.raises(ValueError): pack([1])
    with pytest.raises(TypeError): recode_bytes([0])
