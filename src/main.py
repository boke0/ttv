import argparse
from parser import Parser
from editor import Editor

parser = argparse.ArgumentParser(
    prog='ttv',
    usage='Give the path to text file and path to output video.',
    description='Text-to-Video',
    epilog='end',
    add_help=True
)

parser.add_argument('-i', '--input', 'path to input text file')
parser.add_argument('-o', '--output', 'path to output video file')
parser.add_argument(
    '-s',
    '--speaker',
    'path to directory contains speaker pictures'
)


def main(input: str, output: str, manju: str, ):
    parser = Parser()
    editor = Editor()
    parsed = parser.parse_from_file(input)
    editor.edit(parsed, output)
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    main(
        args.input,
        args.output,
        args.manju,
    )
