#!/usr/bin/env python3
"""tests for jump.py"""

from subprocess import getstatusoutput

prg = './jump.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput('{} 123-456-7890'.format(prg))
    assert rv == 0
    assert out == '987-604-3215'


# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(
        '{} "That number to call is 098-765-4321."'.format(prg))
    assert rv == 0
    assert out.rstrip() == 'That number to call is 512-340-6789.'
