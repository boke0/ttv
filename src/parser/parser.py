from script import Script, FrontMatter, Section, SubSection
import re


class Parser:
    def parse_from_file(self, input_file_path: str) -> Script:
        with open(input_file_path) as f:
            f.read()
        return self.parse(input_file_path)

    def parse(self, input: str) -> Script:
        script = Script()
        section = None
        subsection = None
        buffer = []
        state = 'FRONT_MATTER'

        reg = {
            'front_matter_end': re.compile(r'^[-=]+$')
        }

        for line in input.split('\n'):
            if state == 'FRONT_MATTER':
                if reg['front_matter_end'].match(line) is not None:
                    front = FrontMatter(buffer)
                    script.set_front_matter(front)
                    buffer = []
                    state = ''
                else:
                    buffer.append(line)
            elif state == 'SECTION':
                matched_title = reg['section_title'].match(line)
                if matched_title is not None:
                    section.set_body(self.parse_body(buffer))
                    script.add_section(section)
                    section = Section()
                    section.set_title(matched_title.group())
                    buffer = []
                    state = 'SECTION'
                    continue
                matched_subtitle = reg['subsection_title'].match(line)
                if matched_subtitle is not None:
                    subsection = SubSection()
                    subsection.set_title(matched_title.group())
                    buffer = []
                    state = 'SUBSECTION'
                    continue
                buffer.append(line)
            elif state == 'SUBSECTION':
                matched_subtitle = reg['subsection_title'].match(line)
                if matched_subtitle is not None:
                    subsection.set_body(self.parse_body(buffer))
                    subsection = SubSection()
                    subsection.set_title(matched_subtitle.group())
                    buffer = []
                    continue
                matched_title = reg['section_title'].match(line)
                if matched_title is not None:
                    section.set_body(self.parse_body(buffer))
                    section.add_sub_section(subsection)
                    script.add_section(section)
                    section = Section()
                    state = 'SECTION'
            else:
                matched_title = reg['section_title'].match(line)
                if matched_title is not None:
                    section = Section()
                    section.set_title(matched_title.group())
                    buffer = []
                    state = 'SECTION'
            pass
        return script

    def parse_body(lines: list):
        return []
