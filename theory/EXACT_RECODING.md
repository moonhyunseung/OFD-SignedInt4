# Decoder commutation and operator compatibility

For offset code c in {0,...,15}, set t=c XOR 8. If c<8, then t=c+8 and the signed decoder gives t-16=c-8. If c>=8, t=c-8<8 and the signed decoder gives t=c-8. Thus D_signed(phi(c))=D_offset(c) for every code. Applying the same XOR twice is the identity, so phi is a bijection. Two packed nibbles occupy disjoint bit fields, hence byte XOR0x88 applies this map independently to both coordinates.

For every unchanged group scale S, multiplication preserves equality. Therefore replacing each offset decode C-8 in DirectK or DirectV by the decoded signed code preserves each term and the sum. This is a pointwise proof, not a claim inferred from sampled floating-point agreement. Tests include -8 even though the usual absmax/7 quantizer normally emits only -7,...,7.

Coordinate permutations require the dual permutation of Q for DirectK and of the output coordinate map for DirectV. Group permutations must move scales with their groups. Negation is not a bijection of the entire signed INT4 set because -(-8)=8 is not representable. Arbitrary rotations/requantization are outside this representation bijection.

The reference codec uses Python integers/bytes. Its exhaustive finite verification does not establish an efficient native signed GPU consumption path. Downstream numerical/timing claims must lock the exact source commits separately.
