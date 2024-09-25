# korean_text_normalizer/normalizer.py

import re
from jamo import h2j, j2h


class KoreanTextNormalizer:
    def __init__(self):
        self.abbreviations = {
            'ㄱㅅ': '감사',
            'ㅎㅇ': '안녕하세요',
            'ㅇㅇ': '네',
        }

    def normalize(self, text):
        text = self._expand_abbreviations(text)
        text = self._correct_spelling(text)
        text = self._normalize_emoticons(text)
        text = self._detect_sentence_boundaries(text)
        return text

    def _expand_abbreviations(self, text):
        for abbr, full in self.abbreviations.items():
            text = text.replace(abbr, full)
        return text

    def _correct_spelling(self, text):
        text = text.replace('됬', '됐')
        return text

    def _normalize_emoticons(self, text):
        # 예: '^_^' -> '😊'
        text = text.replace('^_^', '😊')
        return text

    def _detect_sentence_boundaries(self, text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return ' '.join([s.strip() + ('.' if not s.strip().endswith(('.', '!', '?')) else '') for s in sentences])

    def separate_jamo(self, text):
        """한글 자모를 분리합니다."""
        return h2j(text)

    def combine_jamo(self, text):
        """분리된 한글 자모를 결합합니다."""
        return j2h(text)


# 사용 예시
if __name__ == "__main__":
    normalizer = KoreanTextNormalizer()

    sample_text = "ㅎㅇ! 오늘 날씨가 좋네요ㄱㅅ ^_^ 내일도 날씨가 좋았으면"

    normalized_text = normalizer.normalize(sample_text)
    print(f"원본 텍스트: {sample_text}")
    print(f"정규화된 텍스트: {normalized_text}")

    jamo_separated = normalizer.separate_jamo("안녕하세요")
    print(f"자모 분리: {jamo_separated}")

    jamo_combined = normalizer.combine_jamo(jamo_separated)
    print(f"자모 결합: {jamo_combined}")
