## 1. Given the tokens in a vocab file, loading, preprocessing, and creating a dictionary of the byte array to its frequency
## 2. Initialise the vocab with the byte values, and special tokens
## 3. create a merge stats hashmap, with all adjacent tokens except the special tokens, maintain max of the hashmap
## 4. Choose the max indices, make the new index, update the vocab
## 5. Iterate over the list of keys of the dictionary, and update the pair to a single new index, at both the boundaries, identify
## the previous index and update value -- iterate this for the number of merges
import json
from collections import Counter
from heapq import heappop, heappush, heapify
import re
from tqdm.auto import tqdm
from collections import defaultdict

class BPE:
    def __init__(self, filename=None):

        if filename is None:
          self.vocab = [chr(i) for i in range(256)] ## initially include all possible characters to the bytes
          self.merges = {} #list of all the merges we do, along with the index of the specific vocab
          self.special_tokens = {}
        else:
          with open(filename, 'rt') as f:
            self.vocab, merges_keys, merges_values, self.special_tokens = json.load(f)
            self.special_tokens = {int(el):v for el,v in self.special_tokens.items()} #json stores as strings
            self.merges = {tuple(k):v for k,v in zip(merges_keys, merges_values)}

    @staticmethod
    def merge_pair(word, a, b, merged):
        ### BEGIN YOUR CODE
        # word is a list of token_ids
        # for every bigram in the word, if it matches ab, merge it , and replace with merged (new token_id), and return the new list
        for i in range(len(word)-1):
          if i>=len(word)-1:
            break
          if word[i] == a and word[i+1]== b:
            word[i:i+2] = [merged]   # replace with the merged token_id
        return 
      
    def replace_special_tokens(self, word):
  
        # print(self.special_tokens)
        for k,v in self.special_tokens.items():
          # print(k,v)
          word = word.replace(v, chr(k))
        return word

    def train(self, text, target_vocab_size):

        freq_words = Counter(re.findall(r'(?:^|\s)\S+', text))
        
        # freqs = defaultdict(int) #faced keyerror since I was trying to update value without key being present; this ensures initiliasation of 0 to the keys
        words = [[ord(cr) for cr in self.replace_special_tokens(word) if ord(cr) not in self.special_tokens] for word,cnt in freq_words.items() if cnt>1]
        word_counts = [v for v in freq_words.values() if v>1]
        ## Counter cannot hash a list

        # TODO: using a priority queue (maxheap)
        # maxheap = [] # stores the frequency of bigram (freq, tuple(a,b)) across the text document
        while len(self.vocab) < target_vocab_size:
          freqs = Counter()
          for word, countword in zip(words, word_counts):
            
            for (a,b) in zip(word[:-1], word[1:]):
              
              freqs[(a,b)] += countword
          
          a,b = max(freqs, key = freqs.get)
          # print(a,b)
          for word in words:
            
            self.merge_pair(word, a, b, len(self.vocab))
            
          self.merges[(a,b)] = len(self.vocab)
          self.vocab.append(self.vocab[a]+ self.vocab[b]) # a, b are integers, which would be the indices of the corresponding characters
        for k,v in self.special_tokens.items():
          self.vocab.append(v) 
        self.vocab += [""]*(max(self.special_tokens)-len(self.vocab)+1)
        for k, v in self.special_tokens.items():
          self.vocab[k] = v
        return


    def encode(self, text):
        freq_words = Counter(re.findall(r'(?:^|\s)\S+', text))
        tokens = []
        words = [[ord(cr) for cr in self.replace_special_tokens(word)] for word,cnt in freq_words.items()]
        for word in words:
          while True:
            pairs = [
                pair
                for pair in zip(word[:-1], word[1:])
                if pair in self.merges
            ]
            if not pairs:
                break

            min_indx = min(pairs, key=self.merges.get)
            if not min_indx:
              break
            self.merge_pair(word, min_indx[0], min_indx[1], self.merges[min_indx])
          tokens += word
        return tokens


    def decode(self, tokens):
        ## given a set of tokens, map it to characters
        text = ""
        text += "".join([self.vocab[t] for t in tokens])
        return text

    def save(self, fname):
        with open(fname, 'wt') as f:
          json.dump([self.vocab, list(self.merges.keys()), list(self.merges.values()), self.special_tokens], f)
