import jieba
import re
import json
from collections import Counter

def main():
    words = ""
    commentlist = []
    for line in open('./comments.json',encoding='utf-8'):
        line.strip('\n')
        line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
        list = jieba.cut(line,cut_all=False)
        words+=(" ".join(list))
    allwords = words.split()
    counter=Counter()
    for word in allwords:
        if len(word)>1 and word != '\n\r':
            counter[word] += 1
    for i,j in counter.most_common(100):# 输出词频最高词
        comment = {}
        comment["name"] = i
        comment["value"] = j
        commentlist.append(comment)
    with open('result.json','a',encoding='utf-8') as file:
        file.write(json.dumps(commentlist, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
