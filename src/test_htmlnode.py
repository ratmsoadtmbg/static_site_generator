import unittest

from htmlnode import HTMLNode

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
    

if __name__ == "__main__":
    unittest.main()