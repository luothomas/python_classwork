text = "Standing here, I realize, you were just like me, try to make history. But whose to judge, the right from wrong? When our gaurd is down, I think we'll both agree."
for char in text:
    if char in "~!@#$%^&*()_+`-=[]{}|;:'\",./<>?":
        text=text.replace(char, '')

text=text.lower()
text=text.split()
word_counter={}     
for word in text:
    word_counter[word]=word_counter.get(word, 0)+1

print(word_counter)
