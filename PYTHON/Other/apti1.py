a=10
b=20
print("Before a=",a)
print("Before b=",b)

# logic code
a=a+b
b=a-b
a=a-b
print("After a=",a)
print("After b=",b)

a,b=b,a
print("After a=",a)
print("After b=",b)

a=a^b
b=a^b
a=a^b


# Count the ovels in a string
string="rihan"
ovels="aeiouAEIOU"
count=0
for str in string :
    if str in ovels :
        count+=1
print("Ovels:",count)





# check wether 2 strings are anagrams
# cat=act   listen=Silent  earth=heart

str1="listen"
str2="silent"
str1=list(str1)
str2=list(str2)
str1.sort()
str2.sort()
if str1==str2:
     print("Anagrams")
else:
    print("Not Anagram")

    


