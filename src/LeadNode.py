from HTMLNode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag:str=None, value:str=None, props:dict=None) -> None
        super.__init__(tag, value, props)

        if(self.value == None):
            raise ValueError
        


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    