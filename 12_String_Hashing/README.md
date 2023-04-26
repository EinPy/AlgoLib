# STRING HASHING #

Hash functions exists in kryptography,
they can for instance take a string input of any length, and give
a unique output of certain length"

The reason you it is called a rolling hash is that if we look at a
subsegment of a given array you can remove the first one using some
math and ord('some character') * 256^n.

To check if one string exists in another, you can double the first string,
and check if the second one exists in the second. This can be accomplished
by a rolling string hash. 

If you want to chech if a certain segment contains some characteres in no
particular order, you can do a rolling unordered hash. For instance, to find
a subsegment iwth a certain sum. 