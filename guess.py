""""This program have 10 chance to serch
hiddian number and 10 chance after call game over
 and you got number you win tha match"""
n = 100
t = 10
i = 0
count = 1
while i<=9:

    print("Enter the number ?\n")
    a = int(input())
    if(a==n):
        print("You guess right number.\nand won the match.\n You take chance {}".format(count))

        break
    if (i == 9):
        print("all chance are complete \n and Lost the game")
        break
    if(a<n):
        print("please ! enter higher number \n and remaing chance {}".format(t-count))
        count = count + 1
        i = i + 1
        continue
    elif (a > n):
        print("please ! enter lower number\n reamaing chance {}".format(t - count))
        count = count + 1
        i = i + 1
        continue
    # if(count == 10):
    #     print("You take all chance \ngame over !")
    #     i = i + 1
    #     break
    # if(count==10):
    #
    #     count = count + 1
    #     i = i + 1
    #     break



    count = count + 1
    i = i + 1
