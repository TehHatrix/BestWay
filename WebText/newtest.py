from WebText.string_matching import rabin_karp
import re

stopfile = open("stopword.txt", "r")
wordfile = open("secondfile.txt", encoding='utf-8')
stopfile = stopfile.read().split()
word = wordfile.read().lower()
wordcheck = re.sub(r"[^A-Za-z0-9 '\n]+", '', word)

wordline = wordcheck.splitlines()

data = {}

for j in range(len(wordline)):
    wordcheck = wordline[j]
    if not wordcheck:
        continue
    wordcheck = ' ' + wordcheck + ' '
    for stopcheck in stopfile:
        stopcheck =' ' + stopcheck + ' '
        result = rabin_karp(wordcheck, stopcheck, 256, 101)
        if result:
            temp = 0
            for i in result:
                i = i - temp
                wordcheck = wordcheck[:i+1] + wordcheck[i+len(stopcheck):]
                temp += len(stopcheck) - 1
    wordline[j] = wordcheck

r = open("newfile.txt", 'w')


for i in range(len(wordline)):
    r.write(wordline[i] + '\n')
r.close()




