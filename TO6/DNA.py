#Exercise: Write a function, kmers, which returns a list of all k-mers in a given string for a specific k:

def k_mer(x,k):
    kmer_list=[]
    for i in range(len(x)-k+1):
        kmer_list.append(x[i:i+k])
    return kmer_list

#Exercise: Often, we're only interested in unique k-mers. Write a function, unique_kmers, which only returns unique k-mers.
def unique_kmers(x,k):
    uni_kmer_list=[]
    for i in range(len(x)-k+1):
        if x[i:i+k] not in uni_kmer_list:
            uni_kmer_list.append(x[i:i+k])
    return uni_kmer_list

#Exercise: Now try to write a function that returns a list of all k-mers paired together with the number of occurrences of that k-mer in the string. Consider it a bonus if you return the list sorted according to the number of occurrences.

def unique_kmer_count(x,k):
    kmer_dict={}
    for i in range(len(x)-k+1):
        if x[i:i+k] not in kmer_dict:
            kmer_dict[x[i:i+k]]=0
        kmer_dict[x[i:i+k]]+=1
    return kmer_dict

#print(unique_kmer_count('agtagtcg',3))

#Exercise: Complete the exercise described in the template repository about codon translation.
CODON_MAP = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
             'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
             'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 
             'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 
             'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
             'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
             'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
             'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 
             'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 
             'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
             'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 
             'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
             'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 
             'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 
             'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
             'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

def codon_translate(x):
    protein=''
    for i in range(0,len(x)-2,3):
        codon=x[i:i+3]
        protein+=CODON_MAP[codon]
    return protein

print(codon_translate('ATGACCGAACAGTAG'))