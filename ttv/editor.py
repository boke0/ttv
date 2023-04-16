from character import Character
from chapter import Chapter
from command import Heading, Image, Caption, Bgm, Speech, Reset
from voicevox import VoiceVox
from moviepy import AudioFileClip, TextClip, afx, concatenate_videoclips


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
        self.voicevox = VoiceVox
        self.clips = []

    def build(self):
        self.clips = []
        self.add_title_slide()
        self.add_chapters()
        self.set_bgm()
        self.clips[0].write_videofile("output_video.mp4")

    def add_title_slide(self):
        title_voice = AudioFileClip(
            self.voicevox.synthesize_speech(
                self.title,
                self.characters[0].speaker
            )
        )
        title_slide = TextClip(
            title=self.title,
            fontsize=70,
            color="black",
            size=(1920, 1080),
            bg_color="white"
        ).set_duration(title_voice.duration + 1)
        self.clips.append(title_slide.set_audio(title_voice))

    def add_chapters(self):
        for chapter in self.editor.chapters:
            for command in chapter.commands:
                if isinstance(command, Heading) and command.level == 1:
                    self.add_heading(command)
                elif isinstance(command, Image):
                    self.add_image(command)
                elif isinstance(command, Caption):
                    self.add_caption(command)
                elif isinstance(command, Bgm):
                    self.change_bgm(command)
                elif isinstance(command, Speech):
                    self.add_speech(command)
                elif isinstance(command, Reset):
                    self.reset(command)

    def add_heading(self, heading):
        title_voice = AudioFileClip(
            self.voicevox.synthesize_speech(
                heading.text,
                self.characters[0].speaker,
            )
        )
        title_slide = TextClip(
            title=self.title,
            fontsize=70,
            color="black",
            size=(1920, 1080),
            bg_color="white"
        ).set_duration(title_voice.duration + 1)
        self.clips.append(title_slide.set_audio(title_voice))

    def add_image(self, command):
        pass

    def set_bgm(self, command):
        final_video = concatenate_videoclips(self.clips)
        if self.bgm:
            bgm = AudioFileClip(self.bgm).fx(
                afx.loop,
                duration=len(self.clips)
            )
            final_video.set_audio(
                final_video.audio.set_start(0).fx(
                    afx.audio_loop,
                    duration=len(self.clips)
                ).volumex(0.5).overlay(bgm)
            )
        self.clips = [final_video]
        pass
