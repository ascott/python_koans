#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

__ = "-=> FILL ME IN! <=-"

class ___(Exception):
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):

    def _baseAssertEqual(self, first, second, msg=None):
        """Override the exception message when the koan hasn't be attempted.

        Instead of showing a message like:
            "-=> FILL ME IN! <=-" != 4
        Show:
            Please attempt this koan to get more help

        This will force the student to attempt the exercise before giving
        them the answer.
        """
        old_longMessage = self.longMessage
        if first in (__, ____) or second in (__, ____):
            msg = 'Please attempt this koan to get more help'
            try:
                self.longMessage = False
                return super()._baseAssertEqual(first, second, msg)
            finally:
                self.longMessage = old_longMessage
        return super()._baseAssertEqual(first, second, msg)

    def assertNoRegexpMatches(self, text, expected_regex, msg=None):
        """
        Throw an exception if the regular expresson pattern is not matched
        """
        if isinstance(expected_regex, (str, bytes)):
            expected_regex = re.compile(expected_regex)
        if expected_regex.search(text):
            msg = msg or "Regexp matched"
            msg = '{0}: {1!r} found in {2!r}'.format(msg, expected_regex.pattern, text)
            raise self.failureException(msg)
