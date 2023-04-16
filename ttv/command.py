class Header:
    """チャプターやシーンごとのタイトルを表します。

    levelが1の場合、チャプターの区切りを表し、チャプター先頭に蓋絵が挿入されます。
    levelが2の場合、シーンの区切りを表し、タイトルが指定の位置(デフォルトで左上)に表示されます。
    シーンの状態は"--"でリセットされますが、タイトルはlevel2のHeadingが新しく登場しない限り変更されません。
    levelが3以上の場合、キャプションと同じく、内容として表示されます。

    Attributes:
        level (int): ヘッダーのレベル。
        text (str): ヘッダーのテキスト。
    """

    def __init__(self, level=1, text=""):
        self.level = level
        self.text = text


class Image:
    """画像や動画を表示します。

    動画の場合、再生が終わるまで再生し続けます。
    以下のパラメータで表示方法を調整できます。
    resize: "contain" | "cover" | "auto"。表示方法(デフォルトは"auto")。
    bg: bool。背景として使用するかどうか(デフォルトはFalse)。
    start: MM:DD。動画の開始時間。
    end: MM:DD。動画の終了時間。
    focus: bool。動画が終わるまで次のコマンドに遷移しないかどうか。
    repeat: bool。繰り返し再生するかどうか(focusがTrueの場合はFalse)。

    Attributes:
        path (str): 画像または動画ファイルへのパス。
        resize (str): 画像/動画の表示方法。
        bg (bool): 画像を背景として使用するかどうか。
        start (str): 動画の開始時間。
        end (str): 動画の終了時間。
        focus (bool): 動画が終わるまで次のコマンドに遷移しないかどうか。
        repeat (bool): 動画を繰り返し再生するかどうか。
    """

    def __init__(self, path, params=dict()):
        self.path = path
        self.resize = params["resize"] or "auto"
        self.bg = params["bg"] or False
        self.start = params["start"] or None
        self.end = params["end"] or None
        self.focus = params["focus"] or False
        self.repeat = params["repeat"] or False


class Speech:
    """キャラクターの発言内容を表します。

    表情が変化すると、アセットが設定されている場合にはそのアセットに表示が変わります。

    Attributes:
        name (str): キャラ
        expression (str): キャラクターの表情。
        text (str): 発言内容。
    """

    def __init__(self, name, expression="default", text=""):
        self.name = name
        self.expression = expression
        self.text = text


class Caption:
    """テキストで内容を表示します。

    Markdownをパースした形でスライドのように表示されます。

    Attributes:
        text (str): キャプションのテキスト。
    """

    def __init__(self, text):
        self.text = text


class Bgm:
    """BGMを指定のものに切り替えます。

    "--"でリセットし、もとのBGMに戻ります。

    Attributes:
        path (str): BGMファイルへのパス。
    """

    def __init__(self, path=""):
        self.path = path


class Reset:
    """リセットコマンドを表します。"""
    pass
