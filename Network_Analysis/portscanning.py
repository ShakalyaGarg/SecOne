from re import findall
from os import system
system('cmd /c nmap -oN C:\\Users\\sjosi\\Desktop\\output.txt -A 127.0.0.1')
regex = r"[0-9][0-9]+/[a-z][a-z]+.*"
with open ('output.txt', 'r') as infile:
    x = infile.read()
    results = findall(regex,x)
with open('filtered_output.txt', 'w') as outfile:
    for match in results:
        outfile.write(match+"\n")
