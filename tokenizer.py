from typing import Dict, List
class Tokenizer:
  def __init__(self,):
    self.vocab: Dict[int, bytes]
    self.merges: Dict[(int, int), int] ## from (index1, index2)-> new_index
  def encode(self,):
    return
  def decode(self,):
    return

class BPETokenizer(Tokenizer):
  def __init__(self,):
    self.super()

  def encode(self, input: string):

  def decode(self, indices: List[int]):

def preprocessing():
  pass
def train_bpe_tokenizer(data: string):
  pass
  
