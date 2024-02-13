#------create and write on files
# passFile= open("writeFile",'w')
# passFile.write("Hello")
# passFile.close()
# -------------------------------------------

# create file with the same content as another file
# f = open('inputFile.txt','r')
# passFile = open('passFile.txt','w')
# passFile.write(f.read())
# f.close()
# passFile.close()
# -------------------------------------------

# f = open('inputFile.txt','r')
# passFile = open('passFile.txt','w')
# for line in f:
#     line_split = line.split()
#     if line_split[2] == 'P':
#         passFile.write(line)

# f.close()
# passFile.close()
# -------------------------------------------

f = open('inputFile.txt','r')
passFile = open('passFile.txt','w')
failFile =open('FailFile.txt','w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

f.close()
passFile.close()
failFile.close()


