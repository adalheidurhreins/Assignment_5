n = int(input("Enter the length of the sequence: ")) # Do not change this line
step = 1
sum1 = 0
sum2 = 0
sum3 = 0
new_sum = 0

while step <= n:
    if step == 1:
        sum1 = 1
        print (sum1)
    elif step == 2:
        sum2 = 2
        print (sum2)
    elif step == 3:
        sum3 = 3
        print (sum3)
    else:
        new_sum = sum1 + sum2 + sum3
        print (new_sum)
        sum1 = sum2
        sum2 = sum3
        sum3 = new_sum

    step = step+1
