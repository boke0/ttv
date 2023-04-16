class Character:
    def __init__(self, name, config=dict()):
        self.name = name
        self.speaker = config.speaker or None
        self.x = config.x or None
        self.y = config.y or None
        self.expressions = config.expressions or dict()
