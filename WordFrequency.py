SC = [ ',' , '.' ]

with open('sometext.txt') as text:
    for line in text:
        for i in SC:
            line=line.replace(i,"")
        words = line.split()
        wordcount=dict((word,words.count(word)) for word in set (words))

    print(wordcount)