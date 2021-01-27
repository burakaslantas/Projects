f = open("dna3.txt", "r")
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
f = open("dna3_output.txt", "w")
f.write(dna)