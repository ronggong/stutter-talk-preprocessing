"""
Stat of word occurrence,
word information
"""
import os
import sys

def parse_trans(filename):
    with open(filename, 'rb') as f:
        for line in f:
            list_words = line.rstrip().split(' ')
    return list_words

if __name__ == '__main__':
    from male_speaker_id import read_speaker_id
    path_dataset_root = '/Users/ronggong/Documents_using/MTG_document/dataset/LibriSpeech/'
    path_train_clean_100 = os.path.join(path_dataset_root, 'train-clean-100')
    path_speaker_id = os.path.join(path_dataset_root, 'SPEAKERS.TXT')

    male_speaker_ids = read_speaker_id(path_speaker_id)
    
    dict_word_occurrence = {}
    dict_word_info = {}
    for male_id in male_speaker_ids:
        for sub_dir in os.listdir(os.path.join(path_train_clean_100, male_id)):
            if sub_dir != '.DS_Store':
                for filename in os.listdir(os.path.join(path_train_clean_100, male_id, sub_dir)):
                    if '.lab' in filename:
                        filename_absolute = os.path.join(path_train_clean_100, male_id, sub_dir, filename)
                        list_words = parse_trans(filename_absolute)
                        for i, w in enumerate(list_words):
                            w = w.lower()
                            dict_word_occurrence[w] = dict_word_occurrence.get(w, 0) + 1
                            if dict_word_occurrence[w]-1 < 10:
                                dict_word_info[w+'_'+str(dict_word_occurrence[w]-1)] = {'filename': filename.replace('.lab', ''),
                                                                                        'word_idx': i}
    print(dict_word_info)