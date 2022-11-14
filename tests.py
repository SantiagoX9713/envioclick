import unittest
from read_paragraph import read_paragraph, txt

class TestReadParagraph(unittest.TestCase):

    def test_default_count(self):
        self.assertEqual(read_paragraph('logística', paragraph=txt), 4)
    

if __name__ == '__main__':
    unittest.main()