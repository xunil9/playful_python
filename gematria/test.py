#!/usr/bin/env python3
"""tests for gematria.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './gematria.py'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text():
    """Text"""

    out = getoutput('{} "foo bar baz"'.format(prg))
    assert out.strip() == '324 309 317'


# --------------------------------------------------
def test_fox():
    """File"""

    out = getoutput('{} {}'.format(prg, fox))
    assert out.strip() == '289 541 552 333 559 444 321 448 314'

# --------------------------------------------------
def test_sonnet():
    """File"""

    out = getoutput('{} {}'.format(prg, sonnet))
    expected = """
631 107
719 1132

402 215 834 444 771 307 435 438
73 313 527 632 230 771 545
275 765 400 631 444 230 875 534
275 437 450 656 307 546 230 416
729 210 421 227 322 435 422 215 428
816 421 318 421 318 444 747 985
821 440 431 327 307 433 431 538
412 436 73 451 549 964 537
306 215 537 886 656 656 966
510 73 542 221 422 307 431 230 545
389 227 321 426 213 517 213 318 749
404 659 532 548 559 213 746 417
295 341 552 438 1048 435 645 645
401 431 73 549 227 614 230 545 444 540
    """.strip()
    assert out.strip() == expected
