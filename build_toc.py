#!/home/mm/anaconda/envs/mlbook/bin/python

def process_file(in_file, out_file):
    mdFile = open(in_file, encoding='utf-8', mode= 'r')
    toc = []
    levels = [0, 0, 0, 0]
    newFile = open(out_file, encoding='utf-8', mode= 'w')
    tempFile = []
    tocLoc = 0
    partOfToc = False

    for line in mdFile:
        if partOfToc and line != '\n':
            continue
        else:
            partOfToc = False
        if 'Table of Contents' in line:
            tocLoc = len(tempFile) + 1
            partOfToc = True
        elif line[0] == '#':
            secId = build_toc(line, toc, levels)
            line = add_section_tag(clean_line(line), secId) + '\n'
        tempFile.append(line)

    for line in toc:
        tempFile.insert(tocLoc, line)
        tocLoc += 1

    for line in tempFile:
        newFile.write(line)

    mdFile.close()
    newFile.close()


def add_section_tag(line, secId):
    startIndex = line.find(' ')
    line = line[:startIndex + 1] + '<a id=\'' + secId + '\' />' + line[startIndex + 1:]
    return line


def build_toc(line, toc, levels):
    line = clean_line(line)
    secId = 's'
    if line[:4] == '####':
        raise UserWarning('Header levels greater than 3 not supported')
    elif line[:3] == '###':
        levels[3] += 1
        secId += str(levels[1]) + '-' + str(levels[2]) + '-' + str(levels[3])
        toc.append('      * [' + line[4:] + '](#' + secId + ')\n')
    elif line[:2] == '##':
        levels[2] += 1
        levels[3] = 0
        secId += str(levels[1]) + '-' + str(levels[2])
        toc.append('  * [' + line[3:] + '](#' + secId + ')\n')
    elif line[:1] == '#':
        levels[1] += 1
        levels[3] = levels[2] = 0
        secId += str(levels[1])
        toc.append('* [' + line[2:] + '](#' + secId + ')\n')
    return secId


def clean_line(text):
    text = strip_new_line(text)
    text = remove_anchors(text)
    return text


def strip_new_line(text):
    return text.replace('\n', '')


def remove_anchors(text):
    while ('<' in text and '>' in text):
        leftTag = text.index('<')
        rightTag = text.index('>')
        text = text[0:leftTag] + text[rightTag + 1:]
    return text


if __name__ == "__main__":
    process_file(inFile, outFile)