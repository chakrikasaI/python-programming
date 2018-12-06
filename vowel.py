temp = input(" ")
if temp.isalpha()==True:
  if(temp=='A' or temp=='a' or temp=='E' or temp=='e' or temp=='I' 
  or temp=='i' or temp=='O' or temp=='o' or temp=='U' or temp=='u'):
    print("Vowel")
  else:
    print("Consonant")
else:
    print("invalid")
