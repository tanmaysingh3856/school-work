#for counting the lowercase letters
slr = "EnterTHESentence"
lowercase = 0
for i in range(0, len(slr)):
    if slr[i].islower():
        lowercase += 1

print("NUMBER OF LOWERCASE LETTER", lowercase)