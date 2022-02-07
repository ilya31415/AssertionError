import unittest
import functions
from unittest.mock import patch, Mock


class Test_Check_document_existance(unittest.TestCase):

    def test_check_document_existance_True(self):
        for i in functions.documents:
            self.assertTrue(functions.check_document_existance(i["number"]))

    def test_check_document_existance_False(self):
        doct = [{"number": "123"}, {"number": "1245243"}, {"number": "1236546"}]
        for i in doct:
            self.assertFalse(functions.check_document_existance(i["number"]))


class Test_Get_doc_owner_name(unittest.TestCase):
    @patch('builtins.input', return_value='10006')
    def test_get_doc_owner_name(self, mock_user_doc_number):
        self.assertEqual(functions.get_doc_owner_name(), "Аристарх Павлов")


class Test_Show_document_info(unittest.TestCase):
    @patch('builtins.print')
    def test_print(self, mock_print):
        data = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        functions.show_document_info(data)
        mock_print.assert_called_with('passport "2207 876234" "Василий Гупкин"')


class Test_Get_all_doc_owners_names(unittest.TestCase):

    def test_get_all_doc_owners_names(self):
        self.assertEqual(functions.get_all_doc_owners_names(),
                         {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'})

    @unittest.skip('Test_Get_all_doc_owners_names: test_keyError не работает')
    def test_keyError(self, ):
        pass
        self.assertEqual(functions.get_all_doc_owners_names(), {'Василий Гупкин'})


class Test_Add_new_doc(unittest.TestCase):
    list_data = functions.documents

    @patch('functions.documents', return_value=list_data)
    @patch('builtins.input', side_effect=['9', 'd lessons', 'Random Person', '1'])
    def test_add_new_doc(self, data, data2):
        self.assertEqual(functions.add_new_doc(), '1')


class TestRemoveDocFromShelf(unittest.TestCase):

    def test_remove_doc(self):
        """ Удаление документа из Полки """
        self.assertNotIn(functions.remove_doc_from_shelf('10006'), functions.directories)

    def test_type_input(self):
        """Проверка на type входных данных"""
        self.assertRaises(TypeError, functions.remove_doc_from_shelf, ['asda'])
        self.assertRaises(TypeError, functions.remove_doc_from_shelf, {'s': 'sd'})


class TestAddNewShelf(unittest.TestCase):
    pass


class TestDeleteDoc(unittest.TestCase):

    def setUp(self) -> None:
        self.number = '11-2'
        self.list_data = functions.documents

    rr = functions.documents

    @patch('functions.documents')
    @patch('builtins.input')
    def test_return_doc(self,  doc,list_data):
        """ Проверка на возврат удаленных данных """
        rr = functions.documents
        list_data.return_value = rr
        doc.return_value = self.number
        data = [data['number'] for data in self.list_data if self.number in data['number']]
        self.assertEqual(functions.delete_doc(), (data[0], True))
        print(data[0], True)


class TestMoveDocToShelf(unittest.TestCase):
    pass


class TestAddNewDoc(unittest.TestCase):
    pass
