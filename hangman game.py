import random
#مراحل هانج مان 
hangman_stages =[
  '''
    +---+
    |   |
        |
        |
        |
        |
  =========
  ''',
  '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
  ''', 
  '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
  ''',
  '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
  ''', 
  '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
  ''',
  '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
  ''',
  '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========='''
  
]
words=["good", "hello","stop", "ugly"]
random_word=random.choice(words)
#اعرض مسافات بنفس عدد الحروف
display=["_"]*len(random_word)
print(''.join(display))
lives = 6
#قائمة لتخزين الحروف التي تم تخمينها سابقا 
guessed_letters =[]
print(hangman_stages[0])
#اطلب تخمين الحرف
while "_" in display and lives > 0 :
  guessed=input("please guess a letter:").lower()
  #هل الحرف تم تخمينه قبل ذلك
  if guessed in guessed_letters:
    print("you already guessed that .try again.")
    print(f"you have {lives} more tries")
    continue
    #في حالة لم يسبق تخمينه . ضيفه للقائمة
  guessed_letters.append(guessed)
  if guessed not in random_word:
    lives-=1
    print(hangman_stages[6-lives])
#لو صحيح بدل المسافة بحرف و اعرض
  for position in range(len(random_word)):
    if random_word[position] == guessed:
      display[position] = guessed
  print(display)
  print(f"you have {lives} more tries")
if lives ==0:
    print("""
           ******
           you lose
           ******
           """)
    print(hangman_stages[-1])
else:
    print("""
          ******
          YOU WIN
          ******
          """) 
  



    
    
  
  







