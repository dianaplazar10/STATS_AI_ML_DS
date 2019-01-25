'''
This program needs to print of a sum of first 100 numbers.

However, to make it more generic, We cd do the below steps
Create a list and pass that list which had the numbers we are looking to sum
Then pass thsi list to a generic method, that iterates and icrement a sum variable,
for all the values in the list

 (1) function to sum first 100 numbers
 (2) function to sum first n numbers
'''

#(2)
#-- add first n interegers.
def sumFirstNnumbers(n):
    sum=0
    for s in range(0,n+1): # note that.. in range, second param in not inclusive, hence, (n+1)
       sum=sum+s
    print("*******sum for sumFirstNnumbers : ",sum)
#output : 5050, when n =100

#(1)
def sumFirst100():
    sum=0
    for s in range(0,101):
       sum=sum+s
    print("*******sum for sumFirst100 : ",sum)
#output : 5050


sumFirst100()
sumFirstNnumbers(10)
