#!python

from redact_problem import redact_words
import unittest

class RedactTest(unittest.TestCase):
	def test_basic(self):
		sentance = ['hello','world','goodbye','planet']
		redacted = ['goodbye','yes']
		modified = ['hello','world','planet']
		prog_modified = redact_words(sentance, redacted)
		assert prog_modified == modified

	def no_redacted(self):
		sentance = ['this','wont','change']
		redacted = []
		prog_modified = redact_words(sentance, redacted)
		assert prog_modified == []

if __name__ == '__main__':
	print('yea')
	unittest.main()
