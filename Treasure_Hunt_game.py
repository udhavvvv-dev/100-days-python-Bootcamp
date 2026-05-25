#link(https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("L or R? ")
if road == "R":
    print("Dead")
elif road == "L":
    s1 = input("S or W: ")
    if s1 == "S":
        print("Dead")
    elif s1 == "W":
        s2 = input("Which Door? R, B, Y, exit: ")
        if s2 == "exit":
            print("Dead")
        elif s2 == "B":
            print("Dead")
        elif s2 == "R":
            print("Dead")
        else:
            print("Win")