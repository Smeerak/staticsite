from HTMLNode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag: str = None, children: list = None, props: dict = None) -> None:
        super().__init__(tag, children, props)

    def to_html(self):
        if(self.tag):
            #recurse
            pass
        else:
            raise ValueError("No tag found")
        
        if(self.children == None):
            raise ValueError("No children found")
        ##sdfasdfsadfsdfsdfd