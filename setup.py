from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="korean-text-normalizer",
    version="0.1.0",
    author="Oh Jongjin",
    author_email="5jx2oh@gmail.com",
    description="A tool for normalizing Korean text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oh-JongJin/korean_text_normalizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'jamo>=0.4.1',
    ],
)
