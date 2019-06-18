import unittest
import io

from cmds import cat, echo, wc
from src import Environment, TextQuote


class MyTestCase(unittest.TestCase):
    def test_echo_cat(self):
        first_stream = io.StringIO()
        second_stream = io.StringIO()
        third_stream = io.StringIO()
        env = Environment()
        echo([TextQuote("hello", "'")], first_stream, second_stream, env)
        second_stream.seek(0)
        cat([], second_stream, third_stream, env)
        third_stream.seek(0)
        self.assertEqual(third_stream.read(), "hello\n")

    def test_echo_wc(self):
        first_stream = io.StringIO()
        second_stream = io.StringIO()
        third_stream = io.StringIO()
        env = Environment()
        echo([TextQuote("hello", "'")], first_stream, second_stream, env)
        second_stream.seek(0)
        wc([], second_stream, third_stream, env)
        third_stream.seek(0)
        self.assertEqual(third_stream.read(), "1 1 5\n")


if __name__ == '__main__':
    unittest.main()
