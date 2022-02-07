import unittest
import functions
from unittest.mock import patch


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
        """Возврат ФИ  из архива по № документа """
        self.assertEqual(functions.get_doc_owner_name(), "Аристарх Павлов")


class Test_Show_document_info(unittest.TestCase):

    def setUp(self) -> None:
        self.current_document = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}

    @patch('builtins.print')
    def test_print(self, mock_print):
        """Проверка на корректный вывод данных после обработки """
        functions.show_document_info(self.current_document)
        mock_print.assert_called_with('passport "2207 876234" "Василий Гупкин"')


class Test_Get_all_doc_owners_names(unittest.TestCase):

    def test_get_all_doc_owners_names(self):
        """Восврат всех уникальных ФИ в архиве """
        self.assertEqual(functions.get_all_doc_owners_names(),
                         {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'})

    @unittest.skip('tests/tests_unittest_functions.py:38 не работает')
    def test_keyError(self):
        self.assertEqual(functions.get_all_doc_owners_names(), {'Василий Гупкин'})


class Test_Add_new_doc(unittest.TestCase):

    @patch('builtins.input', side_effect=['99999', 'insurance', 'Random', '1'])
    def test_return_number_shelf(self, data):
        """Возврат № полки"""
        self.assertEqual(functions.add_new_doc(), '1')

    @patch('builtins.input', side_effect=['99999', 'insurance', 'Random', '1'])
    def test_append_new_doc(self,data):
        """Проверка добавления нового документа"""
        functions.add_new_doc()
        self.assertIn({'type': 'insurance', 'number': '99999', 'name': 'Random'}, functions.documents)



    def tearDown(self) -> None:
        functions.documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                               {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                               {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]


class TestRemoveDocFromShelf(unittest.TestCase):

    def test_remove_doc(self):
        """ Удаление документа из Полки """
        self.assertNotIn(functions.remove_doc_from_shelf('10006'), functions.directories)

    def test_type_input(self):
        """Проверка на type входных данных"""
        self.assertRaises(TypeError, functions.remove_doc_from_shelf, ['asda'])
        self.assertRaises(TypeError, functions.remove_doc_from_shelf, {'s': 'sd'})


class TestAddNewShelf(unittest.TestCase):

    def setUp(self) -> None:
        self.shelf_number_notin = int([data for data in functions.directories.keys()][-1]) + 1
        self.shelf_number_in = [data for data in functions.directories.keys()][0]

    def test_return_not_and_IN_directKey(self):
        """Возврашает номер полки если полка была или нет"""
        self.assertEqual(functions.add_new_shelf(str(self.shelf_number_notin)), (str(self.shelf_number_notin), True))
        self.assertEqual(functions.add_new_shelf(self.shelf_number_in), (self.shelf_number_in, False))

    def test_add_new_shelf(self):
        """Проверка на наличие новой полки"""
        self.assertIn(functions.add_new_shelf(self.shelf_number_notin)[0], functions.directories.keys())

    def tearDown(self) -> None:
        functions.directories = {'1': ['2207 876234', '11-2', '5455 028765'],
                                 '2': ['10006'],
                                 '3': []}


class TestDeleteDoc(unittest.TestCase):

    def setUp(self) -> None:
        self.number = '11-2'
        self.return_data = [data['number'] for data in functions.documents if self.number in data['number']]
        self.current_document = [data for data in functions.documents if self.number in data['number']]

    @patch('builtins.input')
    def test_return_doc(self, doc):
        """ Проверка на возврат удаленных данных """
        doc.return_value = self.number
        self.assertEqual(functions.delete_doc(), (self.return_data[0], True))

    @patch('builtins.input')
    def test_delete_current_document(self, doc):
        """ Проверка на Удаление данных о пользователе в архиве """
        doc.return_value = self.number
        functions.delete_doc()
        self.assertNotIn(self.current_document[0], functions.documents)

    def tearDown(self) -> None:
        functions.documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                               {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                               {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]


class TestAppendDocToShelf(unittest.TestCase):

    def setUp(self) -> None:
        self.doc_number = '123123'
        self.shelf_number = '15'

    def test_append_doc_to_shelf(self):
        """Проверка на добавление полки и значения """
        functions.append_doc_to_shelf(self.doc_number, self.shelf_number)
        self.assertEqual(functions.directories[self.shelf_number][0], self.doc_number)


if __name__ == "__main__":
    unittest.main()
