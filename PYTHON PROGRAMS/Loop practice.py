#fName =input("Enter a first name ")
#sNaMe =input("Enter a surname")



while True:
    print("running while loop")
    check=input("Do you want the loop to continue? Y/N ")
    if check in ("Y","y"):
        fName =input("Enter a first name ")
        sNaMe =input("Enter a surname")
        print("continuing loop")
    else:
        break
    