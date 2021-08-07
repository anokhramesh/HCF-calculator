# A program to Find the HCF or GCF of Two Given Numbers
#HCF  Stands for-Highest Common Factor or GCF Greatest Common Factor
'''Find the HCF of a set of numbers with this calculator which also shows the steps and how to do the work.
Input the numbers you want to find the HCF . For example, Enter first num=2500 ,second num=1000'''
num1 = int(input("Enter First Number\n"))# user in put num1
num2 = int(input("Enter the Second Number\n"))# user in put num2

if num2>num1:#check the condition -num2 is greater than num1 ot not
    min = num1# the value of num2 is greater than num1,assign the value of num1 to variable name-min
else:#  the value of num1 is greater than num2
    min =num2#assign the value of num1 to variable name-min
for i in range(1, min+1):# iterating the loop to 1 to the value of variable min + 1
    if num1 % i ==0 and num2 % i==0:# if remainder of  num1 divided by  i & num2 divided by  i is eual to 0
        hcf =i# assign the value of i to variable name hcf
print( f"The HCF of {num1} and {num2} is {hcf}")#display the value of variable hcf as an answer.