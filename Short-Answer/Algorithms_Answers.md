#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The input `n` will increase the value of variable `a` by around `n**2` with
each iteration. This means that it will take `n` times to exit the while
loop.

Therefore, the input size `n` in this code snippet runs in `O(n)`

b) There is both an outer and inner loop in this function. Also, the inner loop
will double the value of `j` on each iteration of the `while` loop, ensuring that
it will take `n/2` iterations to exit out of the `while`.

With a nested loop, we have a time complexity of `O(n * (n/2))`, which reduces to
`O(n**2)`

c) `bunnyEars` is a recursive function that calls itself recursively and would
have similar a time complexity as fibronacci. Each recursive call
spawns another call that spawns `n-1` other recursive calls on the call stack,
that each spawns another `n-2` recursive calls on the call stack,
that each spawn another `n-3` ... and so forth.

Therefore, given the recursive calls and how they each call the function
n-1 times, this runs in exponential time. I'm not completely certain if
it's exactly `O(2**n)` but that is my best guess until I learn more math for
computer science, which I hope to right after Lambda

## Exercise II

Understand:
The problem is asking us to create an algorithm to minimize the number of
broken eggs assuming the existence of the building, the building has floors,
and there is an ample supply of eggs, and eggs break if they are on a floor
at or above `f`.

Since this is called highest floor, I must assume that the problem
wants the highest value of f since the grading rubric lists that we should use
searching algorithms. I must also assume that we are throwing eggs off at
each floor and trying to see which highest floor causes the eggs to break.

Plan:
Given the currently available information, I could do a linear search through
the floors until I have found the highest floor that doesn't break the egg.

However, the best way would be to use binary search and split the floors in half
to get the mid floor, k, and check whether the kth floor broke an egg,
and if it didn't, we continue by taking the midpoint of the next section,
and checking if the egg dropped from that floor would break, and so on,
until we find the highest floor.

If the egg broke at the first midpoint then we'd search first in the midpoint
between 1 and k-1, and continue to reduce the number of available floors by 2
until we reach the last floor that breaks the egg or there are no more floors to search.
This divide and conquer approach would reduce the time complexity to O(logn).
The linear search would run in O(n), but I would recommend using the binary search method.

Execute:

The optimal solution would be to set the value of `f` to the highest value
possible using a method akin to binary search since that would reduce the number of broken
eggs to the smallest number on average given that we are testing half as many
floors with each go as we continue searching for the one that breaks eggs

Algorithm:

```
pass in a n, start, and end parameters
  n is the number of floors
  start is the start of the search area in range(n)
  end is the end of the search area in range(n)
set the offset to be equal to the (end - start) // 2
set the midpoint to be the start + offset
select the floor_attempt that is equal to range(n)[midpoint] where range is a range of sequential integers from 0 to n-1

while there are floors to search:
if the floor_attempt breaks, search again with a midpoint between start and end-1
else search again with a midpoint between start+1 and end

return the highest floor
```
