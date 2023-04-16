from character import Character
from chapter import Chapter


class Editor:
    def __init__(self, serif=dict()):
        self.title = serif["frontmatter"].get("title") or ""
        self.bgm = serif["frontmatter"].get("bgm") or None
        characters = serif["frontmatter"].get("characters") or dict()
        self.characters = list()
        for name, character in characters.items():
            self.characters.append(Character(name, character))
        self.chapters = list()
        for chapter in serif["chapters"]:
            self.chapters.append(Chapter(chapter))
