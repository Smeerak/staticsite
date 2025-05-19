#imports
from textnode import TextNodeType
from textnode import TextNode

#main func
def main():
    test = TextNode("This is anchor text", TextNodeType.LINKS , "https://www.boot.dev")
    print(str(test))

#main execution guard
if __name__ == "__main__":
    main()

