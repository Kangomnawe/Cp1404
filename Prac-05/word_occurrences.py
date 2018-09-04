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

text = "this is a collection of words of nice words this is a fun thing it is"

fnneme = input("Enter you file name: ")
if len(fnneme) < 1:
    fnneme = 'text.txt'
file = open(fnneme)

di = dict()

for lin in file:
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
