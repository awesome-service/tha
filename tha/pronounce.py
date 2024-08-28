# Edge TTS miss pronounce words
pronounce_dict = {
  "ឧបនាយក​": "អ៊ុប៉ៈនាយក់",
  "​អតីត": "អៈ-ដិត",
  "​របស់​អតីត": "​របស់​អៈ-ដិត",
  # correct pronounce with space
  "ហ្វូណន": "ហ្វូណន ",
  "មហិមា": "មៈ-ហិ-មៀ",
  "ទេវកថា": "ទេ-វៈ-កៈ-ថា",
}


def processor(text: str):
  for k, v in pronounce_dict.items():
    text = text.replace(k, f"{v} ({k})")
  return text
