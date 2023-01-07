

words = {}
for _ in range(int(input())):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
for v in words.values():
    print(v,end=',')

# def word_order(n,i):
#     count= {}
#     l=[]
#     for i in range(n):
#         word = input()
#         l.append(word)
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#
#     return (len(count))
#     return ' '.join([str(count[word]) for word in count])