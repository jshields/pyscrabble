# pyscrabble
## Give letters, get words.

Python 3.5

Disclaimer: The Unix dictionary used for this does contain some weird "words"
like individual letters and chemical symbols.

## Usage:

Directly from the command line:

    python pyscrabble.py apclaer

Interactive mode:

    python pyscrabble.py

As a Python module:

    import pyscrabble
    pyscrabble.scrabble('koolcake', pyscrabble.build_word_list())


## Post-mortem analysis of the project:

### Initial approach

My initial solution was written with the attitude that "computers are fast."
I brute-forced the solution using the `itertools` module in such a way that the
complexity of the algorithm was:

n * (n-1) * (n-2) * (n-3) ... * 1
"n factorial"
O(n!)

The solution took a few seconds and worked correctly on shorter inputs,
but brought the interpreter to a halt on longer inputs. Not good!

### Revised solution

The general approach of the revised program is,
"the current word must be completely built using the input letters."

I don't consider the list of dictionary words as being input;
the performance analysis will be based strictly on change in performance with change in user input.

Another caveat is that I am considering the Python `in` operator as having to iterate over each item in the righthand operand.
So for the purpose of this review, that is how I will consider it in terms of algorithm complexity.

I reduced the complexity of my algorithm to:
n + (n-1) + (n-2) + (n-3) ... 1
"arithmetic series"
O(n^2)

The arithmetic series comes from the fact that, at each step, one of the input letters is consumed.
We start with having to look at all the input letters `n` to determine if the first letter of the word can be found.
If we find a match for the first word letter, we consume that letter from the currently available input letters before the next step,
to avoid double matches on that letter.
This makes the next pass have `n-1` letters from the original input to look over,
and so on.
The available input letters resets for each dictionary word,
making the actual runtime complexity more than just the arithmetic series on its own.
However, this will be a constant factor (number of words in the dictionary),
which is ignored in Big Oh notation.
