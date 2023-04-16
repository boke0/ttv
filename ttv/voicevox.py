import requests


class VoiceVox:
    def __init__(self, api_key):
        self.api_key = api_key

    def synthesize_speech(self, text, speaker):
        url = "https://deprecatedapis.tts.quest/v2/voicevox/synthesis"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"text": text, "speaker": speaker}

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.content
