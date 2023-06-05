#txt - the sentence 
#word_one - the word to replace
#word_two - word_one replacement  
def word_replacement(txt, word_one, word_two):
    return (txt.replace(word_one, word_two))

txt = 'My name is Daddy Sudad'

newtxt = word_replacement(txt, 'Daddy', "Musa")

print(newtxt)
print(txt)