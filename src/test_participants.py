from participants import process_names, prompt_participants
from unittest.mock import patch
import unittest

class TestProcessing(unittest.TestCase):
    def test_processing_valid_6(self):
        valid_6 = "Charlie, Isi, Céline, Sabi, Roseline, Reto"
        result = process_names(valid_6)
        self.assertEqual(set(result), {"Charlie", "Isi", "Céline", "Sabi", "Roseline", "Reto"})

    def test_processing_invalid_8(self):
        invalid_8 = "Charlie, Isi, Céline, Sabi, Roseline, Reto, Mascia, Esti"
        with self.assertRaises(ValueError):
            process_names(invalid_8)
    
    def test_processing_invalid_3(self):
        invalid_3 = "Charlie, Isi, Céline"
        with self.assertRaises(ValueError):
            process_names(invalid_3)

    def test_processing_invalid_duplicates(self):
        invalid_duplicates = "Charlie, Isi, Céline, Sabi, Céline"
        with self.assertRaises(ValueError):
            process_names(invalid_duplicates)

    def test_processing_whitespaces(self):
        whitespace_input = "Charlie ,  Isi , Céline, Sabi,  Roseline, Reto "
        result = process_names(whitespace_input)
        self.assertEqual(set(result), {"Charlie", "Isi", "Céline", "Sabi", "Roseline", "Reto"})

    def test_processing_empty_string(self):
        empty_string = "Charlie, , Isi, Céline, Sabi"
        with self.assertRaises(ValueError):
            process_names(empty_string)


class TestInput(unittest.TestCase):
    @patch('builtins.input', return_value="Charlie, Isi, Céline, Sabi, Roseline, Reto")
    def test_valid_6(self, mock_input):
        result = prompt_participants()
        self.assertEqual(set(result), {"Charlie", "Isi", "Céline", "Sabi", "Roseline", "Reto"})
        
    @patch('builtins.input', side_effect=['Charlie, Isi, Céline, Sabi, Roseline, Reto, Mascia, Sevi, Esti', 'Charlie, Isi, Céline, Sabi, Roseline, Reto, Mascia, Sevi', 'Charlie, Isi, Céline, Sabi, Roseline, Reto'])
    def test_9_8_7(self, mock_input):
        result = prompt_participants()
        self.assertEqual(set(result), {"Charlie", "Isi", "Céline", "Sabi", "Roseline", "Reto"})
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['Charlie, Isi, Céline', 'Charlie, Isi, Céline, Sabi'])
    def test_3_4(self, mock_input):
        result = prompt_participants()
        self.assertEqual(set(result), {"Charlie", "Isi", "Céline", "Sabi"})
        self.assertEqual(mock_input.call_count, 2)
        
    @patch('builtins.input', side_effect=['Charlie, Isi, Céline, Sabi, Céline', 'Charlie, Isi, Céline, Sabi, Roseline'])
    def test_duplicate(self, mock_input):
        result = prompt_participants()
        self.assertEqual(set(result), {"Charlie", "Isi", "Céline", "Sabi", "Roseline"})
        self.assertEqual(mock_input.call_count, 2)