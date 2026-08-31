from fetch_data import fetch_genbank, fetch_uniprot, fetch_pdb

record = fetch_genbank("NM_000546")
print(record.id, "-", record.description)

# Test error handling with a deliberately bad ID
bad_record = fetch_genbank("FAKE_ID_12345")
print(bad_record)
