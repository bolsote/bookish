from io import BytesIO

import requests
from PIL import Image


class Response:
    def __init__(self, data):
        self.data = data

    @property
    def title(self):
        return self.data['title']

    @property
    def author(self):
        author_list = [
            author['name'].strip() for author in self.data['authors']
        ]
        return ', '.join(author_list)

    @property
    def date(self):
        return self.data['publish_date']

    @property
    def cover(self):
        image_url = self.data['cover']['large']
        image = requests.get(image_url)

        saved_image = f'static/{self.data["identifiers"]["isbn_13"][0]}.png'
        Image.open(BytesIO(image.content)).save(saved_image)

        return saved_image
