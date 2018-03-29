import os
import sys
import epub2wavenet
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Audio book from epub.')
    parser.add_argument('-l', '--list', action='store_true', help='List all voices')
    parser.add_argument('-e', dest='epub', action='store', help='Epub filepath')
    parser.add_argument('-g', dest='gender', default='male',
        help='Gender of the voice [default male]')
    parser.add_argument('-v', dest='voice_id', default='en-US-Wavenet-C',
        help='Google Text to speech API Voice_id [see list for options]')
    parser.add_argument('dir', nargs='?', default=os.getcwd(),
        help='Destination directory [default CWD]')
    args = parser.parse_args()
    if args.list:
        epub2wavenet.list_voices()
    elif args.epub:
        epub2wavenet.generate(args.epub, args.dir, args.voice_id, args.gender)
    else:
        parser.print_help()
