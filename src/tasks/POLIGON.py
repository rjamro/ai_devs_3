import requests


class Task(object):
    @classmethod
    def execute(self) -> list[str]:
        print('POLIGON Task execution')
        response = requests.get(url='https://poligon.aidevs.pl/dane.txt')

        data = response.content.decode()

        return data.strip('\n').split('\n')
