with open("Poem.txt", "w") as f:
    f.write("""
    This is a poem
    and the right thing about poem is that it can be itself .
    a poem through and through .
    """)

word_count={}
with open("Poem.txt", "r") as g:
    for line in g:
        word= line.split()
        for y in word:
            if y in word_count:
                word_count[y]+= 1
            else:
                word_count[y]= 1
print(word_count)

word_count_list= list(word_count.values())
max_word_count= max(word_count_list)

for word, word_count_number in word_count.items():
    if word_count_number== max_word_count:
        print(f"The word that occurs the most in the poem is {word}.")
