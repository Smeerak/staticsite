from HTMLNode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag:str=None, value:str=None, props:dict=None) -> None:
        super().__init__(tag, value, None ,props)

    def to_html(self):
        if(self.value == None):
            raise ValueError
        
        if(self.tag == None):
            return(f"{self.value}")

        if(self.props):
            attribute_str = ""
            for key, val in self.props.items():
                temp_str = f" {key}=\"{val}\""
                attribute_str += temp_str

            return(f"<{self.tag}{attribute_str}>{self.value}</{self.tag}>")

     
        return(f"<{self.tag}>{self.value}</{self.tag}>")




