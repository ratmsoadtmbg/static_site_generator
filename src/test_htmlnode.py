import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "h1", 
            "awesomesauce", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
            )
        node_test = node.props_to_html()
        node_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node_test, node_result)

    def test_repr(self):
        node = HTMLNode(
            "h1", 
            "awesomesauce", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
            )
        node_test = node.__repr__()
        node_result = "HTMLNode: h1, awesomesauce, None, {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(node_test, node_result)

    def test_none(self):
        node = str(HTMLNode(None, None, None, None))
        node_result = "HTMLNode: None, None, None, None"
        self.assertEqual(node, node_result)

    def test_none_props(self):
        node = HTMLNode(None, None, None, None)
        node_test = node.props_to_html()
        node_result = ""
        self.assertEqual(node_test, node_result)
    
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link", {"href": "google.com"})
        self.assertEqual(node.to_html(), '<a href="google.com">This is a link</a>')

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node_test = node.to_html()

if __name__ == "__main__":
    unittest.main()