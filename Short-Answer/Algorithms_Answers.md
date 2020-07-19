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
at or above `f`

There is still some information missing from the description that would help
me to better understand the function and how it would operate. For instance,
it would help to know when the eggs are thrown off and how frequently they
are thrown off. Is it once per floor, or is it at a specified interval? This
information is not listed in the problem so I can't use it to create an
optimal solution.

Plan:
Given the currently available information, I can only control for one variable,
and that is the player's current floor, which I will call `floor_player`.
Regardless of how often eggs are dropped, the best way to minimize the number
of broken eggs is to get the player or thing dropping the eggs to a floor that
is less than `f`. Therefore, the optimal solution will be to reduce the player's
floor as soon as possible to minimize how many eggs break. To figure out the
optimal floor `f` in an `n` story building on which the least eggs break, it would be
any floor less than `f`.

For simplicity, I will assume that the eggs are carried by the person, player,
or actor that is dropping them and thus contained by that object

Execute:

The optimal solution would be to set the value of `f` to the highest value
possible. Since eggs break at height `f` or above, and there are `n` floors,
then we should set `f` == `n`. This operation would ensure that all eggs
dropped would not break, which would minimize the amount of eggs dropped to 1
if we can only set `f` equal to a maximum of `n`.

If there is no way to set `f` equal to `n` because of the stipulation of it
being >= `f` and this requires there to be a floor above `f`, then it would be
optimal to set `f` equal to `n-l`.

This would be somewhat close to a greedy approach and could potentially occur
in O(1) if we merely set the value of `f` to equal to the desired value of `n`/`n-l`
as per the above.

Reflect:

There are some brute force methodologies that we could use, such as assuming some
dynamics of the problem to be true. For instance, if we assumed that one egg was
thrown by floor, and there were 10 total floors, then we could add up the
eggs broken when ascending the floors from 0 based on the value of `f` as below:

n = 10

```
Total Eggs Broken     `f`
------------------    ---
0                     11
1                     10
2                     9
3                     8
4                     7
5                     6
6                     5
7                     4
8                     3
9                     2
10                    1
```

Therefore, the optimal solution is to set `f` equal to `n+l` if possible,
otherwise, based on the constraints of the problem, set it to the highest
possible value closest to `n` such that it satisfies all constraints

Algorithm:

```
def reduce_broken_eggs(f, n):
    f = n + 1
    return f
```

I have no idea how this would actually be accomplished in a concrete example.
Maybe setting higher values of `f` equal to `n` is possible by putting eggs
in little easter baskets with parachutes. I can only speak to what the
problem specification detailed and there are no further details with which
to design the optimal solution.
