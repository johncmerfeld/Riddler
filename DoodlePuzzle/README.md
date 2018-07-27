# DoodlePuzzle

## The challenge
From Renaud Dubedout, a puzzle perfect for doodling during a boring class or meeting, not that I would ever endorse that sort of thing:

Start with an empty 5-by-5 grid of squares, and choose any square you want as your starting square. The rules for moving through the grid from there are strict:

1. You may move exactly three cells horizontally or vertically, or you may move exactly two cells diagonally.
2. You are not allowed to visit any cell you already visited.
3. You are not allowed to step outside the grid.

You win if you are able to visit all 25 cells.

Is it possible to win? If so, how? If not, what are the largest and smallest numbers of squares you can legally visit?

## Strategy
Brute force! Recursively check every possible move. Let's see how long that takes... 
