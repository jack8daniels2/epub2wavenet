import epub
from bs4 import BeautifulSoup

class Book(object):
    def __init__(self, filename):
        self._book = epub.open(filename)
    def __iter__(self):
        for item_id, _ in self._book.opf.spine.itemrefs:
            yield self._book.get_item(item_id)
            # if item.media_type == 'application/xhtml+xml':
            #     data = book.read_item(item)
            #     yield data
    def __str__(self):
        return self._book.toc.title
    def __getitem__(self, item_id):
        return self._book.read_item(self._book.get_item(item_id))

if __name__ == "__main__":
    import sys
    book = Book(sys.argv[1])
    print str(book)
    for item in book:
        print type(item)
        contents = book[item.identifier]
        print "Item {} type {} len {}".format(item.identifier, item.media_type, len(contents))
        # print BeautifulSoup(contents,  "html.parser").text
