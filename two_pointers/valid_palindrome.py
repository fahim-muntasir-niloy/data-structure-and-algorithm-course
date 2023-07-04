word = "race_CaR"
word = word.lower()
# print(len(word))
empty_word = []
rvrs_wrd = []
for i in range(len(word)):
    if word[i].isalnum():
        empty_word.append(word[i])
        rvrs_wrd.append(word[i])

rvrs_wrd.reverse()

if empty_word == rvrs_wrd:
    print(f"{empty_word} Palindrome")
else:
    print(f"{empty_word} not palindrome")

print(rvrs_wrd)