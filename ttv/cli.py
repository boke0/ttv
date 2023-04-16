import argparse
import pprint
from parse import parse_markdown
from editor import Editor


def main():
    args = parse_args()
    filename = args.filename
    with open(filename) as f:
        doc = f.read()
    pprint.pprint(Editor(parse_markdown(doc)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='ttv',
        description='Text to Video',
    )

    parser.add_argument('filename')

    args = parser.parse_args()
    return args
