codes={'A':'`','B':'~','C':'!','D':'@','E':'#','F':'$','G':'%','H':'^','I':'&','J':'*','K':'(','L':')','M':'-','N':'_','O':'=','P':'+','Q':'[','R':'{','S':']','T':'}','U':'|','V':'<','W':'>','X':'/','Y':'?','Z':';'}

infile = open('info_security.txt','r')

outfile=open('encrypted.txt','w')

data=infile.read()
data=data.upper()

for k,v in codes.items():
    search=k
    replace=v

    data=data.replace(search,replace)

outfile.write(data)    