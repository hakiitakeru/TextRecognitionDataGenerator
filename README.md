# TextRecognitionDataGenerator [![CircleCI](https://circleci.com/gh/Belval/TextRecognitionDataGenerator/tree/master.svg?style=svg)](https://circleci.com/gh/Belval/TextRecognitionDataGenerator/tree/master) [![PyPI version](https://badge.fury.io/py/trdg.svg)](https://badge.fury.io/py/trdg) [![codecov](https://codecov.io/gh/Belval/TextRecognitionDataGenerator/branch/master/graph/badge.svg)](https://codecov.io/gh/Belval/TextRecognitionDataGenerator) [![Documentation Status](https://readthedocs.org/projects/textrecognitiondatagenerator/badge/?version=latest)](https://textrecognitiondatagenerator.readthedocs.io/en/latest/?badge=latest)

A synthetic data generator for text recognition

## 変更点
- wiki-40bをダウンロードし、文節区切りするutilを追加(createUtils.py)
- GeneratorFromStringsで、色, フォント, 文字の太さ, 背景をランダムに選んで画像生成できるように変更
  
## ランダムに選べる要素
- width: 文字の太さ intのリスト
- color: 文字の色 strのリスト カラーコードを渡す
- background: 背景 intのリスト 自作の画像を背景にすることもできる
- fonts: フォント strのリスト フォントファイルへのパスをリストにする

dataset.ipynbを参考にしてください