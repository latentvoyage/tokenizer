The vocab is essentially a dictionary of integer to the bytes, and the merges of 2 indices to give a new index is also stored. These constitute the tokenizer data class which is used in its encode and decode methods
The training algorithm is as follows:
1. initialise the vocab dict, merges
2. From the given string corpus --> encode --> map to int (this is the initial list of indices)
3. Run a For loop on the indices array --> construct a maxheap of the frequency of each adjacent pair in the given data --> pass the most frequent occurring adjacent indices --> generate the new index
4. Merge all occurrences of these indices
5. Update the vocab, and merge list

During the tokenization process:
Encoding:
1. 
