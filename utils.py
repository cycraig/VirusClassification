import pandas as pd
import re

def loadFASTA(file_location):
    """Loads a FASTA file into a Pandas DataFrame.
    
    Extracts the ID, Description, and Sequence of each entry.
    Lower case letters are removed from DNA/RNA sequences.
    """
    
    with open(file_location) as f:
        raw_fasta  = f.read()
    data = raw_fasta.split(">")
    # dump the epmpy string in position [0]
    data = data[1:]
    data = [x.split("\n", 1) for x in data]
    
    # separate names and sequences
    id = []
    description = []
    genome_sequences = []
    for x in data:
        # extract ID, Description and Sequence
        id_description = x[0].split(' ', 1)
        id.append(id_description[0])
        description.append(id_description[1])
        genome_sequences.append(x[1])
    
    # clean genome sequences
    clean_sequences = []
    for seq in genome_sequences:
        seq = re.sub('[a-z]', '', seq)  # remove lower case letters
        seq = seq.strip()
        seq = seq.replace('\n', '')
        clean_sequences.append(seq)
        
    # return dataframe
    datalist = [list(x) for x in zip(id,description,clean_sequences)]
    dataframe = pd.DataFrame(datalist, columns = ['ID' , 'Description', 'Sequence'])
    return dataframe
