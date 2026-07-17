from typing import Dict, List
import regex as re
from dataclasses import dataclass
@dataclass
class BPETokenizerData:
  def __init__(self):
    self.vocab: Dict[int, bytes] = {}
    self.merges: Dict[(int, int), int] = {} ## from (index1, index2)-> new_index

## 1. Given the tokens in a vocab file, loading, preprocessing, and creating a dictionary of the byte array to its frequency
## 2. Initialise the vocab with the byte values, and special tokens
## 3. create a merge stats hashmap, with all adjacent tokens except the special tokens, maintain max of the hashmap
## 4. Choose the max indices, make the new index, update the vocab
## 5. Iterate over the list of keys of the dictionary, and update the pair to a single new index, at both the boundaries, identify
## the previous index and update value -- iterate this for the number of merges

class Tokenizer:
  def __init__(self,):
    self.bpedata = BPETokenizerData()
  def encode(self,):
    return
  def decode(self,):
    return

class BPETokenizer(Tokenizer):
  def __init__(self,):
    self.super()

  def encode(self, input: str):
    pass
  def decode(self, indices: List[int]):
    pass
  def preprocessing(self, text:str):
    reg  = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""


def train_bpe_tokenizer(data: str):
  pass
  
