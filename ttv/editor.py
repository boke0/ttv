from character import Character
from scene import Scene


class Editor:
    def __init__(self, serif=dict()):
        self.title = serif["frontmatter"]["title"] or ""
        self.bgm = serif["frontmatter"]["bgm"] or None
        characters = serif["characters"] or dict()
        self.characters = list()
        for name, character in characters.entries():
            self.characters.append(Character(name, character))
        self.scenes = list()
        for scene in serif["scenes"]:
            self.scenes.append(Scene(scene))
