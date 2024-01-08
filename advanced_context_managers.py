import unittest
import os
#1
class CustomFileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        print(f"File '{self.filename}' opened. Counter: {self.counter}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            self.counter -= 1
            print(f"File '{self.filename}' closed. Counter: {self.counter}")
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with message: {exc_value}")
        return False  

filename = 'example.txt'

with CustomFileContextManager(filename, 'r') as file:
    content = file.read()
    print(content)

with CustomFileContextManager(filename, 'w') as file:
    file.write("Hello, World!")


with CustomFileContextManager(filename, 'r') as file:
    content = file.read()
    print(content)
##########################################################
    
#2
class TestCustomFileContextManager(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as file:
            file.write("Test content")

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_file_read(self):
        with CustomFileContextManager(self.filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "Test content")

    def test_file_write(self):
        with CustomFileContextManager(self.filename, 'w') as file:
            file.write("New content")

        with open(self.filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "New content")

    def test_exception_handling(self):
        with self.assertRaises(Exception):
            with CustomFileContextManager(self.filename, 'r') as file:
                raise Exception("Test exception")

    def test_file_closed_after_exception(self):
        try:
            with CustomFileContextManager(self.filename, 'r') as file:
                raise Exception("Test exception")
        except Exception:
            pass

        self.assertFalse(file.file.readable())

    def test_file_not_found(self):
        non_existent_file = 'non_existent_file.txt'
        with self.assertRaises(FileNotFoundError):
            with CustomFileContextManager(non_existent_file, 'r') as file:
                pass

    def test_multiple_file_operations(self):
        with CustomFileContextManager(self.filename, 'r') as file:
            content1 = file.read()
            self.assertEqual(content1, "Test content")

        with CustomFileContextManager(self.filename, 'w') as file:
            file.write("Updated content")

        with CustomFileContextManager(self.filename, 'r') as file:
            content2 = file.read()
            self.assertEqual(content2, "Updated content")

if __name__ == '__main__':
    unittest.main()