import requests

from bookish.lib.isbn import ISBN
from bookish.lib.response import Response


class Request:
    BASE_URI = 'https://openlibrary.org/api/books'

    def __init__(self, isbn):
        self.isbn = ISBN(isbn)

    @property
    def key(self):
        return f'ISBN:{self.isbn.clean}'

    @property
    def params(self):
        return {
            'bibkeys': self.key,
            'format': 'json',
            'jscmd': 'data',
        }

    def perform(self):
        if not self.isbn.validate():
            raise Exception

        response = requests.get(
            self.BASE_URI, params=self.params
        )
        data = response.json()[self.key]

        return Response(data)
