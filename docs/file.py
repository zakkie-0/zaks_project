# read('r'): Opens for reading.
# Write('w'): Opens for Writing, truncates or creates.
# Append('a'): Opens for writing, appends or creates.
# Read/Write('r+'): Opens for reading and writing.
# Write/Read(w+): Opens for writing and reading, truncates or creates.
# Append/Read(a+): Opens for appending and reading, creates if not exists
#--------------------------------------------------------------------------#
# file = open("doc.txt","r")

# # read, readline, readlines
# content = file.read()

# print(content)

with open("doc1.txt","w+") as file:

    file.writelines("Data 2")
    file.seek(0)
    content = file.read()

    print(content)

    # Name, Phone Number, Email