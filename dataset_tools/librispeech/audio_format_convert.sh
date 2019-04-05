# convert libriSpeech audio from .flac to .wav
# split the .trans.txt for each file and save them into .lab

PATH_ROOT=$1

for p in $PATH_ROOT*
do
    for pp in $p/*
        do 
            for f in $pp/*
            do
                # convert the audio from .flac to .wav
                if [[ $f == *.flac ]]; then
                    ffmpeg -i $f ${f%.flac}.wav
                fi
                # split the .trans.txt for each file and save them into .lab
                if [[ $f == *.trans.txt ]]; then
                    while IFS='' read -r line; do
                        # from the beginning, remove the shortest matching string anything followed by space
                        trans="${line#* }"
                        # from the end, delete the longest match space followed by anything
                        basename="${line%% *}"
                        path="${f%/*}"
                        # write transcription into .lab
                        echo "$trans" > $path/$basename.lab
                    done < $f
                fi
            done
        done
done