import requests


class YandexFolder:
    def __init__(self, token: str):
        self.token = token

    def creating_folders(self, name_folders: str):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        params = {"path": name_folders}
        resource = requests.put(up_url, headers=headers, params=params)
        return resource

    def delete_folders(self, path_folders: str):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        params = {"path": path_folders, "permanently": "true"}
        resource = requests.delete(up_url, headers=headers, params=params)
        return resource

    def headers(self):
        return {'Content-Tape': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
                }


if __name__ == '__main__':
    TOKEN = 'AQAAAAAjmNY6AADLW2BGzDqt1U4yqkOaLvabTos'

    yandex = YandexFolder(token=TOKEN)

    print(yandex.creating_folders('qweqwe'))

    print(yandex.delete_folders('qweqwe'))
