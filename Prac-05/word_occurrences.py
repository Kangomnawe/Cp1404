""" Out put
Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""


text = {1: 'this', 2: 'is', 3: 'a', 4:'collection', 5: 'of', 6: 'words', 7: 'of', 8: 'nice', 9: 'words', 11: 'this',
        12: 'is', 13: 'a', 14: ' fun', 15: 'thing', 16: 'it', 17: 'is'}

word = input("Enter you any word: ")
if len(word) < 1:
    word = 'text'
# pass
# text = open(word)
pass
# print(text)

di = dict()

for lin in text:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            print("count")
        print(w, di[w])
