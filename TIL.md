# Things I Learned

## Day 3

chunk a list into groups of n: `zip(*[iter(my_list)] * n)`
- creates a list of n iterators, but they are all the same iterator
- as zip unpacks that list, it calls the iterator three times