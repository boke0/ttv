import re
import yaml

# 正規表現パターン
HEADING_PATTERN = r'^(#+)\s+(.+)$'
CHARACTER_SPEECH_PATTERN = r'^([^\s:]+)(?:\s+\(([^)]+)\))?:(.+)$'
IMAGE_PATTERN = r'^!\[.*\]\((.*)\)$'


# パーサ関数
def parse_markdown(markdown_text):
    # パース結果を格納するリスト
    scenes = []
    frontmatter = None
    # フロントマターを取得する
    frontmatter_pattern = r'(\-+)\n(.*?)\n(\-+)\n'
    frontmatter_match = re.search(
        frontmatter_pattern, markdown_text, re.DOTALL)
    if frontmatter_match:
        frontmatter_text = frontmatter_match.group(2).strip()
        frontmatter = yaml.safe_load(frontmatter_text)
    scene_docs = markdown_text.split("---")

    if frontmatter is not None:
        scene_docs.pop(0)
        scene_docs.pop(0)

    for scene_doc in scene_docs:
        if len(scene_doc.strip()) == 0:
            continue
        result = []
        # 各行をパースする
        for line in scene_doc.splitlines():
            line = line.strip()

            # ヘディングの場合
            if re.match(HEADING_PATTERN, line):
                heading_match = re.match(HEADING_PATTERN, line)
                heading_level = len(heading_match.group(1))
                heading_text = heading_match.group(2)
                result.append({
                    'type': 'heading',
                    'level': heading_level,
                    'text': heading_text
                })

            # キャラクターの台詞の場合
            elif re.match(CHARACTER_SPEECH_PATTERN, line):
                character_speech_match = re.match(CHARACTER_SPEECH_PATTERN, line)
                character_name = character_speech_match.group(1)
                character_expression = character_speech_match.group(2)
                speech_text = character_speech_match.group(3)
                result.append({
                    'type': 'character_speech',
                    'name': character_name,
                    'expression': character_expression,
                    'text': speech_text
                })

            # 画像の場合
            elif re.match(IMAGE_PATTERN, line):
                image_match = re.match(IMAGE_PATTERN, line)
                image_url = image_match.group(1)
                result.append({'type': 'image', 'url': image_url})

            # シーンリセットの場合
            elif line == '--':
                result.append({'type': 'reset'})

            elif line.startswith('BGM:'):
                bgm = int(line.split(':')[1])
                result.append({'type': 'bgm', 'path': bgm})

            # それ以外の場合
            else:
                result.append({'type': 'caption', 'text': line})
        scenes.append(result)
    return {
        "frontmatter": frontmatter,
        "scenes": scenes
    }
