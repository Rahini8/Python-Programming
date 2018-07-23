def swapem (s):
if len(s)<2:
return s
 return "%s%s%s"%(s[1], s[0], swapem (s[2:]))

for str in ("", "a", "ab", "abcd", "abcde"):
    print "[%s] -> [%s]"%(str, swapem (str))
