# Suffix Array
It is a data structure that provides a sorted array of all suffixes of a given string. This allows for efficient string operations such as substring search, pattern matching, and lexicographical ordering.


### LCP array
- There can also be a LCP (Longest Common Prefix) array associated with the suffix array, which stores the lengths of the longest common prefixes between consecutive suffixes in the sorted order. Sum of the LCP array gives the number of duplicate substrings of a string.
-  The highest value in the LCP array gives the length of the longest repeated substring in the string.