from mistletoe.block_token import Document, BlockToken, span_token
import pprint
import re


class Speaker(BlockToken):
    pattern = re.compile(r" {0,3}(?:\n|\s+?(.*?)(?:\s+?:\s*?$))")
    level = 3
    speaker = ''

    def __init__(self, match):
        self.speaker, content = match
        super().__init__(content, span_token.tokenize_inner)

    @classmethod
    def start(cls, line):
        match_obj = cls.pattern.match(line)
        pprint(match_obj)
        if match_obj is None:
            return False
        cls.speaker = match_obj.group(1).strip()
        return True

    @classmethod
    def read(cls, lines):
        next(lines)
        return cls.level, cls.content


def load_from_file(filename: str) -> Document:
    with open(filename, 'r') as f:
        return Document(f)
