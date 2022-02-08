import unittest
import API_yandex
from unittest.mock import patch


class TestAPIYandex(unittest.TestCase):

    def setUp(self) -> None:
        self.token = 'AQAAAAAjmNY6AADLW2BGzDqt1U4yqkOaLvabTos'
        self.attribute = API_yandex.YandexFolder(self.token)
        self.name_folder = 'Unittest'
        self.Response = '<Response [201]>'

    def test_creating_folders(self):

        self.assertEqual(self.attribute.creating_folders('Unittest'), self.Response)

    def tearDown(self) -> None:
        self.attribute.delete_folders(self.name_folder)
