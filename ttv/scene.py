from command import Heading, Image, Speech, Caption, Bgm, Reset


class Scene:
    def __init__(self, serif=list()):
        self.commands = list()
        for command_dict in serif:
            type = command_dict["type"]
            if type == "heading":
                command = Heading(
                    command_dict["level"],
                    command_dict["text"],
                )
            elif type == "character_speech":
                command = Speech(
                    command_dict["name"],
                    command_dict["expression"],
                    command_dict["text"],
                )
            elif type == "image":
                command = Image(command_dict["url"])
            elif type == "reset":
                command = Reset()
            elif type == "bgm":
                command = Bgm(command_dict["path"])
            elif type == "caption":
                command = Caption(command_dict["text"])
            else:
                continue
            self.commands.append(command)
