#isEven using caching or something
import sys, os

def isEven(num):
    pass

theNum = int(sys.argv[1])
isItEven = isEven(theNum)
if isItEven == None:
    with open("main.py", "r") as file:
        with open("new.py", "w+") as file2:
            for line in file:
                file2.write(line)
                if "def isEven" in line:
                    break
            file2.write(f"    if num == {theNum}:\n")
            file2.write(f"        return {theNum % 2 == 0}\n")
            for line in file:
                file2.write(line)
    os.system(f"python3 new.py {theNum}")
    os.system("mv new.py main.py")
else:       
    print(isItEven)