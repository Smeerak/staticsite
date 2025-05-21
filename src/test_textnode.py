import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is not a good node", TextType.CODE, url = "www.woof.com")
        self.assertNotEqual(node, node1)
        
    def test_is_instance(self):
        node = TextNode("This is a text node", TextType.BOLD, url="www.none.com")
        self.assertIsInstance(node, TextNode)

if __name__ == "__main__":
    unittest.main()