import unittest
from HTMLNode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "this is some text")
        node1 = HTMLNode("<p>", "this is some text")
        
        self.assertEqual(node, node1)


    def test_not_eq(self):
        pass

    def test_to_html(self):
        pass


if __name__ == "__main__":
    unittest.main()

