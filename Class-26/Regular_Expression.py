import re

txt ="We on love python"

getspecificseq = re.findall("e", txt)
print(getspecificseq)

searchchar = re.search('python', txt)
print(searchchar)
print(searchchar.span())
print(searchchar.start())
print(searchchar.end())

spilttxt = re.split(' ', txt)
print(spilttxt)

subChar = re.sub(' ', '04', txt)
print(subChar)

