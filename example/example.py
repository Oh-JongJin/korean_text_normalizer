from korean_text_normalizer import KoreanTextNormalizer

normalizer = KoreanTextNormalizer()

text = "ㅎㅇ! 오늘 날씨가 좋네요ㄱㅅ ^_^ 내일도 날씨가 좋았으면"
normalized_text = normalizer.normalize(text)

print(normalized_text)