#HTMLNode Class

class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = None
        for key, val in self.props:
            rtr_string = (f" {key}={val}")
                          

        return(props_string)    

    def __repr__(self) -> str:
        print(f"HTML Node:{self.tag}\Value:{self.value}\nChildren:{self.children}\nProperties:{self.props}")

    def __eq__(self, value: object) -> bool:
        return(True)