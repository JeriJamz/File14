alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print"Yo input something"
response = input()
str_in = response

n = len(str_in)
str_out = ""

for i in range(n):
    c = str_in[1]
    loc = alpha.find(c)
    print i, c, loc,
    newloc = loc + 3
    str_out += alpha[newloc]
    print newloc, str_out

print "Output: ", str_out 



