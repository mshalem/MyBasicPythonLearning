secret_word = "giraffe"
guess = ""
guess_count = 0
while guess != secret_word and guess_count > 3:
    guess = input("Enter your Guess: ")
    if guess != secret_word:
        print ("Your Guess is Wrong, Please Try again")
    guess_count += 1

if guess == secret_word:
    print ("you win!!")
elif guess_count > 3:
    print ("Your chances are over, YOU LOST!!")


##############################################################################################
secret_word = "dog"
ans = ""
ans_count = 0
ans_limit = 3
out_of_ans = False

while ans != secret_word and not(out_of_ans):
    if ans_count < ans_limit:
        ans = input ("enter your ans: ")
        ans_count += 1
    else:
        out_of_ans = True
if out_of_ans:
    print ("you lost, your chances are over")
else:
    print ("You Win!!")

