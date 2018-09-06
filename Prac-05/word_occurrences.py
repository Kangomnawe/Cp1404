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

"""
Text: this is a collection of words of nice words this is a fun thing it is
"""
string = input("Enter string:")
word = input("Enter word:")
a = []
count = 0
a = string.split(" ")
for i in range(0, len(a)):
    if (word == a[i]):
        count = count + 1
print("Count of the word is:")
print(count)






# word = input("Enter you any word: ")
# if len(word) < 1:
#     word = 'text'
# # pass
# # text = open(word)
# pass
# # print(text)
#
# di = dict()
#
# for lin in text:
#     lin = lin.rstrip()
#     # print(lin)
#     wds = lin.split()
#     # print(wds)
#     for w in wds:
#         if w in di:
#             di[w] = di[w] + 1
#         else:
#             di[w] = 1
#             print("count")
#         print(w, di[w])
