a=int(input("Pick a number"))
b=[]
# empty list
# append is a function for list which add a value at the end of the list

while(a > 0):
  c = int(input("Enter a number"))
  b.append(c)
  a = a-1

print(b)

i=0   # first index of the list 
j=len(b)-1  # last index of the list 

# in a list you have some volues, and every value can be accessed using the index of that position
# ex:L= [23, 44, 55, 64, 1234, "abnf"]
#        0   1    2   3   4     5
# Every value in the list will be stored at particular index 
# L[3] ?


while(i < j):
  print("i = ",i ," and j = ",j)
  b[i],b[j] = b[j],b[i]   # swapping the values at index i and j
  i = i + 1
  j = j - 1 

print("value after loop:  i = ",i ," and j = ",j)

print(b)
print (b)

