# Korean Text Normalizer

Korean Text Normalizer is a Python package for normalizing Korean text. It provides various functions to process and clean up Korean text data.



## Features

- Expand common Korean abbreviations
- Perform basic spell checking
- Normalize emoticons
- Detect and correct sentence boundaries
- Separate and combine Korean jamo (syllable characters)



## Installation

You can install the package using pip:

```
pip install korean-text-normalizer
```



## Usage

Here's a basic example of how to use the Korean Text Normalizer:

```python
from korean_text_normalizer import KoreanTextNormalizer

normalizer = KoreanTextNormalizer()

text = "ㅎㅇ! 오늘 날씨가 좋네요ㄱㅅ ^_^ 내일도 날씨가 좋았으면"
normalized_text = normalizer.normalize(text)

print(normalized_text)
```



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.



## License

This project is licensed under the MIT License.
