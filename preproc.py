def generate_fixed_length_chunks(sequence, chunk_length, overlapping=True):
    chunks = []
    if overlapping:
        for i in range(len(sequence) - chunk_length + 1):
            chunks.append(sequence[i:i+chunk_length])
    else:
        for i in range(0, len(sequence), chunk_length):
            chunk = sequence[i:i+chunk_length]
            if len(chunk) == chunk_length:
                chunks.append(sequence[i:i+chunk_length])
    return chunks

def preprocess_file_into_chunks(file_path, chunk_length, overlapping=True):
    with open(file_path, 'r') as file:
        sequences = file.read().splitlines()
    
    all_chunks = []
    for seq in sequences:
        seq_chunks = generate_fixed_length_chunks(seq, chunk_length, overlapping)
        all_chunks.extend(seq_chunks)
    
    return all_chunks

def save_chunks_to_file(chunks, output_file_path):
    with open(output_file_path, 'w') as file:
        for chunk in chunks:
            file.write(f"{chunk}\n")

def preprocess_test_file_into_chunks_and_save(file_path, chunk_length, overlapping=True, i=1):
    with open(file_path, 'r') as file:
        sequences = file.read().splitlines()
    
    chunks_file_path = f'syscalls/snd-cert/snd-cert-chunks-{chunk_length}.{i}.test'
    identifiers_file_path = f'syscalls/snd-cert/snd-cert-chunks-{chunk_length}-identifiers.{i}.txt'
    
    with open(chunks_file_path, 'w') as chunks_file, open(identifiers_file_path, 'w') as identifiers_file:
        for index, seq in enumerate(sequences):
            seq_chunks = generate_fixed_length_chunks(seq, chunk_length, overlapping)
            for chunk in seq_chunks:
                chunks_file.write(f"{chunk}\n")
                identifiers_file.write(f"{index}\n")

i = 3
test_file_path = f'syscalls/snd-cert/snd-cert.{i}.test'
chunk_length = 7  
overlapping = False  

preprocess_test_file_into_chunks_and_save(test_file_path, chunk_length, overlapping, i)

print("Chunks and identifiers have been saved to 'chunks.txt' and 'identifiers.txt', respectively.")

# file_path = 'syscalls/snd-cert/snd-cert.train' 
# chunk_length = 7  
# overlapping = False  
# output_file_path = f'syscalls/snd-cert/snd-cert-chunks-{chunk_length}.train' 

# chunks = preprocess_file_into_chunks(file_path, chunk_length, overlapping)

# save_chunks_to_file(chunks, output_file_path)

# print(f"Generated {len(chunks)} chunks and saved them to {output_file_path}.")
