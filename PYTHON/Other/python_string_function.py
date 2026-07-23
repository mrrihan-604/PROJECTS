Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> str1="GOAT"
>>> str1[1]
'O'
>>> str1[-2:-1]
'A'
>>> str2="RAM"
>>> str1+str2
'GOATRAM'
>>> str1*3
'GOATGOATGOAT'
>>> len(str2)
3
>>> 'py' in str1
False
>>> 'oa' in str1
False
>>> 'OA' in str1
True
>>> str1.lower()
'goat'
>>> str1
'GOAT'
>>> str3="Rihan"
>>> str4="Kani"
>>> str5="Rihan Kani"
>>> str5.lower()
'rihan kani'
>>> str5.upper()
'RIHAN KANI'
>>> str5.capitalize()
'Rihan kani'
>>> str5.swapcase()
'rIHAN kANI'
>>> str5
'Rihan Kani'
>>> str5.split()
['Rihan', 'Kani']
>>> str5.find("iha")
1
>>> str5.index("ihan")
1
>>> str5[4]="n"
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    str5[4]="n"
TypeError: 'str' object does not support item assignment
