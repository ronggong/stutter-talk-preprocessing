# for cleaning xiaohuangji data
# remove 'E ' or 'M ' if it exist at the beginning of a line
# remove blank line

with open('/Users/ronggong/Documents_using/projects/stutterTalk/data/xiaohuangji50w_nofenci.conv', 'r') as conv_file:
    lines = conv_file.readlines()
    lines_no_blank = []
    for l in lines:
        if not l.startswith('E'):
            if l.startswith('M '):
                l = l.replace('M ', '')
                lines_no_blank.append(l)

with open('/Users/ronggong/Documents_using/projects/stutterTalk/data/xiaohuangji50w_nofenci_noblank.txt', 'w') as txt_file:
    for l in lines_no_blank:
        txt_file.write(l)