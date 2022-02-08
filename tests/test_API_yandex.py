import unittest
import API_yandex


class TestAPIYandex(unittest.TestCase):

    def setUp(self) -> None:
        self.token = ''
        self.attribute = API_yandex.YandexFolder(self.token)
        self.name_folder = 'Unittest'
        self.status_code = 201

    def tearDown(self) -> None:
        if self.attribute.delete_folders(self.name_folder).status_code == 404:
            print('Folder is not delete')

    def test_creating_folders(self):
        """Проверка на успешное создания папки на YD
        И на ошибку при попытке повторно создать папку с идентичным именем """

        self.assertEqual(self.attribute.creating_folders(self.name_folder).status_code, self.status_code)
        self.assertEqual(self.attribute.creating_folders(self.name_folder).status_code, 409)

    def test_name_typeError(self):
        """Возврат ошибки при несоответствие type введенных данных """
        self.assertRaises(TypeError, self.attribute.creating_folders, {'Словарь': 'словарь'})
        self.assertRaises(TypeError, self.attribute.creating_folders, ['Список'])
        self.assertRaises(TypeError, self.attribute.creating_folders, {'Словарь', 'словарь'})

    def test_availability_folders(self):
        """Наличие созданной папки """
        self.attribute.creating_folders(self.name_folder)
        self.assertEqual(self.attribute.info_folders(f'disk:/{self.name_folder}').json()['type'], 'dir')

    def test_return_href(self):
        """Вовзрат href в .json"""
        text = self.attribute.creating_folders(self.name_folder).json()['href']
        self.assertRegex(text, r'^https.*')
