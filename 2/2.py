sum = 0
smallerTerm = 1
largerTerm = 1  
while largerTerm < 4000000:
    if(largerTerm % 2 == 0):
        sum += largerTerm
    next = smallerTerm + largerTerm
    smallerTerm = largerTerm
    largerTerm = next
print(sum)