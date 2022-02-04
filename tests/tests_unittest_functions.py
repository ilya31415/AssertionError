import unittest
import functions
from unittest.mock import patch, Mock

class TestCheck_document_existance(unittest.TestCase):

    def test_check_document_existance_True(self):
        for i in functions.documents:
            self.assertTrue(functions.check_document_existance(i["number"]))

    def test_check_document_existance_False(self):
        doct = [{"number": "123"}, {"number": "1245243"}, {"number": "1236546"}]
        for i in doct:
            self.assertFalse(functions.check_document_existance(i["number"]))


    def test_check_(self):

        @patch('builtins.input',return_value=8 )
        def test_check_1(self,mock):
                self.assertEqual(functions.qwe(5),13)

class TestGet_doc_owner_name(unittest.TestCase):
    @patch('builtins.input', return_value='10006')
    def test_get_doc_owner_name(self, mock_user_doc_number):
            self.assertEqual(functions.get_doc_owner_name(), "Аристарх Павлов")



class TestShow_document_info(unittest.TestCase):
    @patch('builtins.print')
    def test_print(self,mock_print):
        data = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        functions.show_document_info(data)
        mock_print.assert_called_with('passport "2207 876234" "Василий Гупкин"')

class Testadd_new_doc(unittest.TestCase):

    def test_add_new_doc(self):

        with unittest.mock.patch('builtins.input', side_effect=['9', 'd lessons', 'Random Person', '1']):
             self.assertEqual(functions.add_new_doc(),'1')

class Testget_all_doc_owners_names(unittest.TestCase):

    def test_get_all_doc_owners_names(self):
        self.assertEqual(functions.get_all_doc_owners_names(), {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'})

