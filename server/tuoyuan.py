# pylint: disable=invalid-name
"""A randomized authenticated encryption mode using the encrypt-then-MAC
   construction, using deniable key exchange on djb's Curve25519.
   It is primarily intended for use with Pythonista on iOS, which supports
   AES encryption via PyCrypto; it does work, however, with any version
   of Python.
   The code for scalar multiplication using a Montgomery ladder is based
   on Matt Dempsey's, in the NaCl crypto paper.
   Note that no provisions for defense against side-channel attacks have been
   made. It is assumed that this code will be used interactively; it is unsafe
   for automated use.
   License: CC0 with attribution kindly requested
"""

from __future__ import division, print_function
import random
import functools

_RINT = functools.partial(random.SystemRandom().randint, 0)
_z = 2 ** 128 -1
#--Curve25519--

P = 2 ** 255 - 19
A = 486662


def inv(x):
  """Invert `x` in F_2*255-19."""
  return pow(x, P - 2, P)


def add((xn, zn), (xm, zm), (xd, zd)):
  """Add two points."""
  x = 4 * (xm * xn - zm * zn) ** 2 * zd
  z = 4 * (xm * zn - zm * xn) ** 2 * xd
  return (x % P, z % P)


def double((xn, zn)):
  """Double a point."""
  x = (xn ** 2 - zn ** 2) ** 2
  z = 4 * xn * zn * (xn ** 2 + A * xn * zn + zn ** 2)
  return (x % P, z % P)


def curve25519(m, base):
  """Scalar multiplication on Curve25519."""
  one = (base, 1)
  two = double(one)
  R0, R1 = one, two
  bits = []
  while m:
    bits.append(m & 1)
    m >>= 1
  bits = bits[::-1]
  for b in bits[1:]:
    if b == 0:
      R1 = add(R0, R1, one)
      R0 = double(R0)
    else:
      R0 = add(R0, R1, one)
      R1 = double(R1)
  x, z = R0
  return (x * inv(z)) % P
print(_RINT(_z))
print(curve25519(174809303557766310774107359041143908071,9))
print(curve25519(174809303557766310774107359041143908071,199006959630016467789854383377875600572))
