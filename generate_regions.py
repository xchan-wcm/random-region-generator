import os
import random

# Define the chromosome lengths for hg19
chrom_lengths = {
    'chr1': 249250621,
    'chr2': 243199373,
    'chr3': 198022430,
    'chr4': 191154276,
    'chr5': 180915260,
    'chr6': 171115067,
    'chr7': 159138663,
    'chr8': 146364022,
    'chr9': 141213431,
    'chr10': 135534747,
    'chr11': 135006516,
    'chr12': 133851895,
    'chr13': 115169878,
    'chr14': 107349540,
    'chr15': 102531392,
    'chr16': 90354753,
    'chr17': 81195210,
    'chr18': 78077248,
    'chr19': 59128983,
    'chr20': 63025520,
    'chr21': 48129895,
    'chr22': 51304566,
    'chrX': 155270560,
    'chrY': 59373566
}

# Set the number of regions to generate
num_regions = 10000

# Generate a list of random regions
regions = []
for i in range(num_regions):
    # Choose a random chromosome
    chrom = random.choice(list(chrom_lengths.keys()))
    # Choose a random start position
    start = random.randint(0, chrom_lengths[chrom])
    # Choose a random end position
    end = random.randint(start, chrom_lengths[chrom])
    # Add the region to the list
    regions.append((chrom, start, end))

# Write the regions to a temporary file
with open('temp.bed', 'w') as f:
    for region in regions:
        f.write('{}\t{}\t{}\n'.format(region[0], region[1], region[2]))

# Sort the regions using bedops
os.system('sort-bed temp.bed > sorted_regions.bed')

# Remove the temporary file
os.remove('temp.bed')
