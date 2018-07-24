def alphabet_value(lowercase):
  c=(ord(lowercase)-96)
  return(c)
word=input().split()
wlen1=len(word[0])
wlen2=len(word[1])
r=0
wlen3=min(wlen1,wlen2)
wlen4=max(wlen1,wlen2)
for i in range(wlen3):
  m=abs(alphabet_value(word[0][i])-alphabet_value(word[1][i]))
  r+=m
if(wlen1>wlen2):
  for i in range(wlen3,wlen1):
    x=alphabet_value(word[0][i])
    r+=x
elif(wlen2>wlen1):
  for i in range(wlen3,wlen2):
    y=alphabet_value(word[1][i])
    r+=y
print(n)

