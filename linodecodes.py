
sentence = "Linode is really cool"
words = sentence.split(' ')

for word in words:
    print ''.join(reversed(word)),
