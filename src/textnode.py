from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code Text'"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"


class TextNode:
    def __init__(self, text:str, text_type:TextType, url:str=None):

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if(self.text == other.text):
            if (self.url == other.url):
                if(self.text_type.value == other.text_type.value):
                    return (True)
        return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")