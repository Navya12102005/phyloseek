from Bio import Entrez, SeqIO

print("Starting fetch...")

Entrez.email = "navyag543@gmail.com"

handle = Entrez.efetch(db="nucleotide", id="NM_000546", rettype="gb", retmode="text")
print("Got response from NCBI")

record = SeqIO.read(handle, "genbank")
print("Parsed record")

print(record.id)
print(record.description)
print(record.seq[:100])