import os
from bs4 import BeautifulSoup
from book_reader import Book
from gcp_api import list_voices, synthesize_text

def generate(epub_file, destination, voice_id='en-US-Wavenet-C', gender=None):
    book = Book(epub_file)
    for chapter_id, chapter in enumerate(book):
        if chapter.media_type == 'application/xhtml+xml':
            text = BeautifulSoup(book[chapter.identifier],  "html.parser").text
        else:
            print 'skipping media_type ', chapter.media_type
            continue
        if not text:
            continue
        sections = filter(len, text.split('\n'))
        if not sections:
            continue
        chapter_dir = os.path.join(destination, 'chapter_{}'.format(chapter_id))
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)
        for section_id, section in enumerate(sections):
            section_file = 'section_{}.mp3'.format(section_id)
            filepath = os.path.join(chapter_dir, section_file)
            synthesize_text(section, filepath, voice_id=voice_id)
