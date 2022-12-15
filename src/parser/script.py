import yaml


class FrontMatter:
    def __init__(self, input: str):
        yml = yaml.load(input)


class SubSection:
    def __init__(self):
        self.title = ''
        self.body = ''
        self.subsections = []

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body


class Section:
    def __init__(self):
        self.title = ''
        self.body = ''
        self.subsections = []

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body

    def add_sub_section(self, subsection: SubSection):
        self.subsections.append(subsection)


class Script:
    def __init__(self):
        self.sections = []
        pass

    def set_front_matter(self, front_matter: FrontMatter):
        self.front_matter = front_matter

    def add_section(self, section: Section):
        self.sections.append(section)
