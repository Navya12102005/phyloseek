from Bio import Entrez, SeqIO
import requests

Entrez.email = "navyag543@gmail.com"

# 1. Fetch from GenBank (DNA/mRNA)
def fetch_genbank(accession_id):
    handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    return record

# 2. Fetch from UniProt (protein)
def fetch_uniprot(uniprot_id):
    response = requests.get(f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta")
    return response.text

# 3. Fetch from PDB (3D structure)
def fetch_pdb(pdb_id):
    response = requests.get(f"https://files.rcsb.org/download/{pdb_id}.pdb")
    return response.text

# Test all three
print("=== GenBank ===")
gb_record = fetch_genbank("NM_000546")
print(gb_record.id, "-", gb_record.description)

print("\n=== UniProt ===")
uniprot_data = fetch_uniprot("P04637")  # P04637 = human p53 protein
print(uniprot_data[:200])

print("\n=== PDB ===")
pdb_data = fetch_pdb("1TUP")  # a real p53-related structure
print(pdb_data[:300])