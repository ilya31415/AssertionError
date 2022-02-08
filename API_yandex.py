

import requests


class YandexFolder:
    def __init__(self, token: str):
        self.token = token

    def creating_folders(self, name_folders):
        if type(name_folders) not in [str, int, float]:
            raise TypeError("Неверный тип данных")
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        params = {"path": name_folders}
        resource = requests.put(up_url, headers=headers, params=params)
        return resource

    def delete_folders(self, path_folders):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        params = {"path": path_folders, "permanently": "true"}
        resource = requests.delete(up_url, headers=headers, params=params)
        return resource

    def info_folders(self, path):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        params = {"path": path,  "permanently": "true"}
        resource = requests.get(up_url, headers=headers, params=params)
        return resource

    def headers(self):
        return {'Content-Tape': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
                }


if __name__ == '__main__':
    TOKEN = ''
    yandex = YandexFolder(token=TOKEN)