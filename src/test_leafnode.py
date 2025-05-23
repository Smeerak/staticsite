import unittest
from LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href":"https://www.me.here", "target":"_blank","class":"my-link"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.me.here\" target=\"_blank\" class=\"my-link\">Click Me!</a>")
        
    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None, {"href":"https://www.me.here", "target":"_blank","class":"my-link"})
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Click Me!", {"href":"https://www.me.here", "target":"_blank","class":"my-link"})
        self.assertEqual("Click Me!", node.to_html())
    