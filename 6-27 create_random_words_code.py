#6/27
import random
open = open("6-27 create_random_words.txt", "r+")
stringy = open.read()
training_words = stringy.splitlines()
induvidual_chars = []
for i in range(len(training_words)):
    induvidual_chars.append(list(training_words[i]+" "))
all_words = []
length = int(input("What length do you want the words to be?: "))
for a in range(int(input("How many words do you want to create?: "))):
    current_word = []
    rand = random.randint(1,len(training_words))
    start_letter = induvidual_chars[rand-1][0]
    current_word.append(start_letter)
    if length > 1:
        for i in range(length-1):
            letters = []
            select_letter = []
            count = []
            for j in range(len(training_words)-1):
                for k in range(len(induvidual_chars[j])-2):
                    try:
                        if current_word[i] == induvidual_chars[j][k]:
                            select_letter.append(induvidual_chars[j][k+1])
                            if (induvidual_chars[j][k+1]) not in letters:
                                letters.append(induvidual_chars[j][k+1])
                    except:
                        pass
            for j in range(len(letters)):
                count.append(int(int(select_letter.count(letters[j]))**1.75))
            rand = random.randint(0,sum(count))
            for j in range(len(letters)):
                if rand < count[j]:
                    current_word.append(letters[j])
                    break
                else:
                    rand -= count[j]
        current_word = ''.join(current_word)
        all_words.append(current_word)
print(all_words)