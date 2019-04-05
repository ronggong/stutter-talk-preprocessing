"""
Parse textgrid, extract no more than 10 samples for each word
"""

import os
import sys
import json
from praatio import tgio
from subprocess import call

if __name__ == '__main__':
    from male_speaker_id import read_speaker_id
    path_dataset_root = '/Users/ronggong/Documents_using/MTG_document/dataset/LibriSpeech/'
    path_train_clean_100 = os.path.join(path_dataset_root, 'train-clean-100')
    path_train_clean_100_word_level = os.path.join(path_dataset_root, 'train-clean-100_word_level')
    path_aligned_train_clean_100 = os.path.join(path_dataset_root, 'aligned_train-clean-100')
    path_current = os.path.dirname(os.path.abspath(__file__))
    path_speaker_id = os.path.join(path_dataset_root, 'SPEAKERS.TXT')

    male_speaker_ids = read_speaker_id(path_speaker_id)

    dict_word_occurrence = {}

    for male_id in male_speaker_ids:
        for sub_dir in os.listdir(os.path.join(path_train_clean_100, male_id)):
            if sub_dir != '.DS_Store':
                for filename in os.listdir(os.path.join(path_aligned_train_clean_100, male_id, sub_dir)):
                    if '.TextGrid' in filename:
                        filename_textgrid = os.path.join(path_aligned_train_clean_100, male_id, sub_dir, filename)
                        filename_audio = os.path.join(path_train_clean_100, male_id, sub_dir, filename.replace('.TextGrid', '.flac'))
                        tg = tgio.openTextgrid(filename_textgrid)
                        words_tier = tg.tierDict["words"].entryList
                        for interval in words_tier:
                            label = interval.label
                            if label == '<unk>':
                                continue
                            label = label.lower()
                            dict_word_occurrence[label] = dict_word_occurrence.get(label, 0) + 1
                            if dict_word_occurrence[label] < 11:
                                filename_audio_output = os.path.join(path_train_clean_100_word_level, label+'_'+str(dict_word_occurrence[label] - 1)+'.flac')
                                start_time = str(interval.start)
                                end_time = str(interval.end-interval.start)
                                call(['ffmpeg', '-ss', start_time, '-t', end_time, '-i', filename_audio, filename_audio_output])