import tensorflow_datasets as tfds
import re
import spacy
import ginza
import pickle
from trdg.generators.from_strings import GeneratorFromStrings

nlp = spacy.load("ja_ginza")

with open("preprocess.pkl", 'rb') as f:
  preprocess_dict = f.load()
  
trans_dict = preprocess_dict["trans_dict"]
removed_kigou = preprocess_dict["removed_kigou"]
kigou = preprocess_dict["kigou"]
stopWords = [i for i in removed_kigou if i not in kigou]
stop_words = r'['+''.join(stopWords)+']'
stop_pattern = re.compile(stop_words)

def preprocess(text):
  processed_text = text.translate(str.maketrans(trans_dict))
  processed_text = stop_pattern.sub('', processed_text)
  processed_text = processed_text.replace('NEWLINE', '')
  return processed_text

def bunsetsuGinza(text):
  doc = nlp(text)
  return [i.text for i in ginza.bunsetu_spans(doc)]

def download_wiki(split):
  return tfds.load(name='wiki40b/ja', split=split, with_info=False)

def create_bunsetsu_list(wiki_data):
  bunsetsu_list = []
  l_extend = bunsetsu_list.extend

  for i, wiki in enumerate(wiki_data.as_numpy_iterator()):
    for text in wiki['text'].decode().split('\n'):
      if (text[:7:]=='_START_'):
        continue
      text = preprocess(text)
      l_extend(bunsetsuGinza(text))
      
  return bunsetsu_list

def create_table(train, val, test):
  train_chars = set(''.join(train))
  val_chars = set(''.join(val))
  test_chars = set(''.join(test))
  
  table_list = sorted(list(train_chars | val_chars | test_chars))
  
  if tacle_list[0] == '':
    table_list.pop(0)
  table_list.insert(0,'<UNK>')
  table_list.insert(-1, '<BLK>')
  
  return table_list

def generate_image(bunsetsu_list,
                   output_path,
                   fonts,
                   width,
                   colors,
                   background,
                   mode='train'):
  i = 0
  ann = []
  digits = len(str(len(bunsetsu_list)))
  
  generator = GeneratorFromStrings(
    bunsetsu_list,
    fonts = fonts,
    count = len(bunsetsu_list),
    stroke_width = width,
    text_color = colors,
    background_type = background
  )
  
  for img, lbl in generator:
    path = output_path+'/word_'+str(i).zfill(digits+1)+'.jpg'
    img.save(path)
    ann.append(path+' '+lbl)
    i+=1
    
  ann_txt = '\n'.join(ann)
  with open('dataset/'+mode+'_annotation.txt', 'w') as f:
      f.write(ann_txt)