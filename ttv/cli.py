import argparse
import md


def main():
    args = parse_args()
    filename = args.filename
    doc = md.load_from_file(filename)
    with md.TTVRender() as r:
        print(r.render(doc))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='ttv',
        description='Text to Video',
    )

    parser.add_argument('filename')

    args = parser.parse_args()
    return args
