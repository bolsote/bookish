from bookish.lib.isbn import ISBN


def test_isbn():
    isbn = ISBN('978-0-099-54094-6')

    assert isbn.validate()
