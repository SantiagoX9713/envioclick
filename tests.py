import unittest
from read_paragraph import read_paragraph, txt
from order_by_criteria import order_by_criteria
from entry import entry, output

class TestReadParagraph(unittest.TestCase):

    def test_default_count(self):
        self.assertEqual(read_paragraph('logística', paragraph=txt), 4)
    

    def test_default_order_by_creiteria(self):
        self.assertEqual(order_by_criteria(), output)


if __name__ == '__main__':
    unittest.main()