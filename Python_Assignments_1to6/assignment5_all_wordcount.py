"""Wordcount exercise
Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import json

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def print_words(file_n):
  with open(file_n, "r") as fl:
    my_file = fl.read().split()
    set_of_words = list(set(my_file))
    word_count_storage = dict()
    for each_word in set_of_words:
      counter = my_file.count(each_word)
      word_count_storage[each_word] = counter
    
    print(word_count_storage)

def print_top(file_n):
  with open(file_n, "r") as fl:
    my_file = fl.read().split()
    set_of_words = list(set(my_file))
    word_count_storage = dict()
    for each_word in set_of_words:
      counter = my_file.count(each_word)
      word_count_storage[each_word] = counter


    for val in sorted(word_count_storage.values(), reverse=True):
      print(val)
    
    print(word_count_storage)

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  print("option ",option)
  print("filename ",filename)
  if option == 'alice.txt':#'--count':
    print_words(filename)
  if option == 'alice.txt':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
