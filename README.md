# random-region-generator
This Python script generates a random set of genomic regions and sorts them using the sort-bed command from the bedops tool suite.

## Requirements

- Python 3
- bedops

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/xchan-wcm/random-region-generator.git
   cd random-region-generator
   ```

2. Run the script:

   ```
   python generate_regions.py
   ```

3. The sorted regions will be saved to a file called `sorted_regions.bed` in the same directory.

## Configuration

- `chrom_lengths`: A dictionary of chromosome lengths for the reference genome. Modify this dictionary to match the chromosome lengths for your reference genome.
- `num_regions`: The number of regions to generate.
- `temp_filename`: The filename of the temporary file used to store the randomly generated regions before sorting.

## Credits

This script was written by [XC](https://github.com/xchan-wcm/).
