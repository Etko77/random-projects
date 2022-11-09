txt = 'I am Iron Man'
small_txt = txt.lower()
big_txt = txt.upper()
big_letters = []
small_letters = []
for i in txt:
    for j in small_txt:
        if i != ' ':
            if i == j:
               small_letters.append(i)
    
    for k in big_txt:
        if i != ' ':
            if i == k:
              big_letters.append(i)

print(big_letters)
print(small_letters)
