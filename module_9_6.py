def all_variants(text):
    x = len(text)
    for j in range(1, x + 1):
        for k in range(x - j + 1):
            yield text[k:k + j]

a = all_variants("abc")
for i in a:
    print(i)