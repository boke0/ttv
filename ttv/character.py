class Character:
    def __init__(self, name, config=dict()):
        self.name = name
        self.speaker = config.get('speaker') or None
        self.x = config.get('x') or None
        self.y = config.get('y') or None
        self.expressions = config.get('expressions') or dict()
