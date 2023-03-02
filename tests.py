import io
import os
import shutil
import unittest
import tempfile

from handler import IOHandler, TimedIOHandler, CountedIOHandler, TimedCountedIOHandler


def multiply():
    num1, num2 = map(int, input().split())
    num3, num4 = map(int, input().split())
    return num1 * num2 * num3 * num4


class TimedIOHandlerTestCase(unittest.TestCase):

    def test_timed_io(self):
        func = TimedIOHandler(multiply)
        self.assertEqual(func('5 6\n2 1'), 60)
        self.assertEqual(func('4 3\n5 2'), 120)


class CountedIOHandlerTestCase(unittest.TestCase):

    def test_counted_io(self):
        func = CountedIOHandler(multiply)
        self.assertEqual(func('5 6\n2 1'), 60)
        self.assertEqual(func('4 3\n5 2'), 120)
        self.assertEqual(func.counter, 2)


class TimedCountedIOHandlerTestCase(unittest.TestCase):

    def test_timed_counted_io(self):
        func = TimedCountedIOHandler(multiply)
        self.assertEqual(func('5 6\n2 1'), 60)
        self.assertEqual(func('4 3\n5 2'), 120)
        self.assertEqual(func.counter, 2)


class IOHandlerWithFileIOTestCase(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.filename = 'test.txt'
        self.dirname = tempfile.mkdtemp()
        self.filepath = os.path.join(self.dirname, self.filename)
        # Write the contest of the file
        with open(self.filepath, 'w') as file:
            file.write('5 4\n3 2')

    def tearDown(self):
        # Remove the temporary directory
        shutil.rmtree(self.dirname)

    def test_file_io(self):
        func = IOHandler(multiply, io.FileIO)
        self.assertEqual(func(self.filepath), 120)


if __name__ == '__main__':
    unittest.main()
