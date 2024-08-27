# Edge TTS miss pronounce words
pronounce_words = {
  "ឧបនាយក​": "អ៊ុប៉ៈនាយក់",
}


def processor(text: str):
  for k, v in pronounce_words.items():
    text = text.replace(k, v)
  return text
