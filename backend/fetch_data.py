from Bio import Entrez, SeqIO
import requests

Entrez.email = "navyag543@gmail.com"

def fetch_genbank(accession_id):
    """Fetch a DNA/mRNA record from GenBank by accession ID."""
    try:
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
        return record
    except Exception as e:
        return f"Error fetching GenBank record: {e}"

def fetch_uniprot(uniprot_id):
    """Fetch a protein sequence from UniProt by ID, in FASTA format."""
    try:
        response = requests.get(f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: UniProt returned status {response.status_code}"
    except Exception as e:
        return f"Error fetching UniProt record: {e}"

def fetch_pdb(pdb_id):
    """Fetch a 3D structure file from PDB by ID."""
    try:
        response = requests.get(f"https://files.rcsb.org/download/{pdb_id}.pdb")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: PDB returned status {response.status_code}"
    except Exception as e:
        return f"Error fetching PDB record: {e}"