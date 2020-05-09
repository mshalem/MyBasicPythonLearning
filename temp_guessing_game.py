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
