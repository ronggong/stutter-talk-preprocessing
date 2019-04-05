# stutter-talk-preprocessing
Preprocessing code for stutter-talk "read as you type" app

## LibriSpeech tools

* `audio_format_convert.sh` convert audio from .flac to .wav, split transcription to line level lab.  
* `male_speaker_id.py` extract the speaker ids from SPEAKER.txt.  
* `trim_audio.py` trim utterance into word level samples using textgrid aligned.  
* `save_mongo_db.py` insert word level samples to mongoDB.