import sys

def read_speaker_id(filename_speaker, sex='M', dataset='train-clean-100'):
    output_id = []
    with open(filename_speaker, 'r') as f:
        for line in f:
            if line[0] != ';':
                ID, SEX, SUBSET, _, _ = line.split(' | ')
                if SEX.strip() == sex and SUBSET.strip() == dataset:
                    output_id.append(ID.strip())
    return output_id

if __name__ == '__main__':
    filename_speaker = '/Users/ronggong/Documents_using/MTG_document/dataset/LibriSpeech/SPEAKERS.TXT'
    output_id = read_speaker_id(filename_speaker)
    print('male speaker ids:', output_id)