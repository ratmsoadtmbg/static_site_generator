import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.youtube.com")
        node_test = "TextNode(This is a text node, italic, https://www.youtube.com)"
        self.assertEqual(str(node), node_test)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is b text node", TextType.IMAGE, "https://urmom.lol")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_wrong_type(self):
        with self.assertRaises(Exception):
            node = TextNode("text node", TextType.BLOD)
        


if __name__ == "__main__":
    unittest.main()