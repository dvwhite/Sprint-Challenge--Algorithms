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
