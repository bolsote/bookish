import pytest
from webtest import TestApp as WebTestApp

from bookish import main


@pytest.fixture
def app():
    app = main({})
    return WebTestApp(app)


def test_search(app):
    response = app.post('/', {
        'isbn': '978-0-099-54094-6',
    })

    assert response.status_int == 200

    result = response.pyquery('div.result')
    
    assert result.children('p.title').text() == (
        'Title: The Master and Margarita'
    )
    assert result.children('p.author').text() == (
        'Author: Михаил Булгаков'
    )
    assert result.children('p.date').text() == (
        'Published: 2004'
    )
    assert result.children('img.cover').attr('src') == (
        'static/9780099540946.png'
    )
