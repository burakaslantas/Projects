#python 3.9
#.::Burak Aslantas::.#
print("############################################")
print("########## Convert DNA To Protein ##########")
print("############################################")
print("Give DNA File => Get Protein File")
print("Note: Given DNA sequence should be without spaces")
requested_file = input("Enter file name including file format:")
file = open(requested_file, "r")
dnaString = file.read()
dnaString = dnaString.upper()
file.close()
print("Given DNA (between '[' and ']') = [" + dnaString + "]")

#Dna Codon Table
codonTable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}
triplets = []
protein = ""
for i in range(0, len(dnaString), 3):
    triplet = dnaString[i:i + 3]
    triplets.append(triplet)
    if codonTable[triplet] == "_" :
        continue
    protein += codonTable[triplet]

requested_file_without_format = requested_file.split(".")
print(requested_file_without_format)
output_file = requested_file_without_format[0] + "_output." + requested_file_without_format[1]
file = open(output_file, "w")
file.write(protein)
print("********************************************")
print("Codons (between '[' and ']') = ", end="")
print(triplets)
print("Protein (between '[' and ']') = [" + protein + "]")
print("Get your protein file '" + output_file + "'")