from pprint import pformat


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
        return self.data['cover']['large']
