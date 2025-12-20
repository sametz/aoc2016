# Things I Learned

## Day 3

chunk a list into groups of n: `zip(*[iter(my_list)] * n)`

- creates a list of n iterators, but they are all the same iterator
- as zip unpacks that list, it calls the iterator three times

## Day 4

Sorting by two criteria, with one ascending and the other descending. 

`c_sorted = sorted(c, key=lambda x: (-x[1], x[0]))`

- reverse sorting of `x[1]` requires it to be numeric

implementing rot-n using a shift table.
```
a = string.ascii_lowercase
    shift = n % 26
    rot_n_table = str.maketrans(a, a[shift:] + a[:shift])
    return s.translate(rot_n_table)
```

## Day 8

Numpy: filling slices; roll
Matplotlib: pyplot `imshow` to visualize array