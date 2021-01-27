requested_file = input("Enter file name including file format:")
f = open(requested_file, "r")
lines = f.readlines()
f.close()

words = []
dna = ""
for line in lines:
    words += line.split()
print(words)
for word in words:
    if word.startswith("g") or word.startswith("c") or word.startswith("a") or word.startswith("t"):
        dna += word

requested_file_without_format = requested_file.split(".")
output_file = requested_file_without_format[0] + "_dna-output." + requested_file_without_format[1]
f = open(output_file, "w")
f.write(dna)