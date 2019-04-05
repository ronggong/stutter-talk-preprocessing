import os
import base64
from tqdm import tqdm
from pymongo import MongoClient

client = MongoClient('mongodb://localhost')

stutter_talk_test = client['stutterTalkMaleLibriSpeech100']
audioBinaries = stutter_talk_test['audiobinaries']

path_root_audio = '/Users/ronggong/Documents_using/MTG_document/dataset/LibriSpeech/train-clean-100_word_level'

filenames_flac = [f for f in os.listdir(path_root_audio) if '.flac' in f]

for flac in tqdm(filenames_flac):
    basename = flac.replace('.flac', '').split('_')
    filename_audio = os.path.join(path_root_audio, flac)
    f = open(filename_audio, 'rb')
    d = f.read()
    d = base64.encodebytes(d)
    dataURI = "data:audio/flac;base64,"+d.decode('ascii')
    doc = {
            "name": basename[0],
            "index": int(basename[1]),
            "data": dataURI
          }
    audioBinaries.insert_one(doc)