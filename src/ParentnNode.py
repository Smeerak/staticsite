from HTMLNode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag: str = None, children: list = None, props: dict = None) -> None:
        super().__init__(tag, children, props)

    def to_html(self):
        if not tag:
            raise ValueError("No tag found")
        elif not self.children:
            raise ValueError("No children found")s
        else: #has a tag and children
            for child in self.children:
                child.to_html()
                
