# Files

# Read mode --> "r"

    # file = open("demo.txt", "r")

    # print(file.read())
    # # print(file.readline())
    # # print(file.readline())
    # # print(file.readline())

    # file.close()

# Append or Write mode --> "a" / "w"

file = open("demo.txt", "a")

file.write("Have a nice day...!")

file.close()