import os
import sys
import unittest

# Find the directory in which the current script resides:
src_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../src'))
sys.path.append(src_dir)

from Quiz.main import Quiz


class TestQuiz(unittest.TestCase):

    def test_nothing(self):

            app = Quiz()



