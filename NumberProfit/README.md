# NumberProfit

### The topline conclusion: The winning strategy is usually to be the lowest-placed token of the group, placed in the middle of the board. Let the other players crowd out the high-value spaces while you sweep up many low-dollar ones.

## [The challenge](https://fivethirtyeight.com/features/step-1-game-theory-step-2-step-3-profit/)
From Steven Pratt, use your econ, win some cash:

Ariel, Beatrice and Cassandra — three brilliant game theorists — were bored at a game theory conference (shocking, we know) and devised the following game to pass the time. They drew a number line and placed $1 on the 1, $2 on the 2, $3 on the 3 and so on to $10 on the 10.

Each player has a personalized token. They take turns — Ariel first, Beatrice second and Cassandra third — placing their tokens on one of the money stacks (only one token is allowed per space). Once the tokens are all placed, each player gets to take every stack that her token is on or is closest to. If a stack is midway between two tokens, the players split that cash.

How will this game play out? How much is it worth to go first?

*A grab bag of extra credits:* What if the game were played not on a number line but on a clock, with values of $1 to $12? What if Desdemona, Eleanor and so on joined the original game? What if the tokens could be placed anywhere on the number line, not just the stacks?

## Workflow
For starters, I thought it'd be fun to make a *real, playable version of the game*, which you can find [here](https://johncmerfeld.github.io/numberProfit.html). I messed around with this for a while and thought I knew what the optimal move for player A was (8), but it was hard to be sure without writing everything down. Therefore, it was time for some [Minimax](https://en.wikipedia.org/wiki/Minimax) game-tree traversal!

Getting the C++ code to compile didn't take long, but I struggled to actually achieve optimal gameplay. At first, I was fooled because the result confirmed my hunch that player A should place her token on space 8, with player B placing her token on 6, also as I thought was optimal. Then I noticed that player C was outfoxing A by placing her token on 9, putting A in last place!

I wondered momentarily whether that wasn't the point of the riddle; that the player who acts first is always at a disadvantage. But there *was* an optimal first placement for A that I found with a smaller experiment: 3 players and 5 spots. In that case, A should (counterintuitively, I thought) place her token on 3, collecting 1+2+3=6 dollars, the most possible.

Eventually, I found the bug in my code by which player A wasn't fully considering player C's possible moves, and the program got up and running properly! I made the output a little more human readable and calculated the average profits for first- and non-first moves, which allowed me to answer the actual question posed by the Riddler! Conveniently, my program could take in any number of players or possible spaces, so I did some meta-analysis.

## The algorithm

Minimax is one of a few things in this universe that is aptly named. In its basic form, we can think of a two-person, zero-sum game, i.e. you want to maximize your score, and I want to minimize your score (thus maximizing my own). When you consider how to move in this simple game, you want to look ahead to what my best move is *from the game state you will create with your potential move*. But to calculate how I'll move, you'll need to look ahead to all the possible moves you might make in response to all of my possible moves!

As you can see, this quickly becomes [computationally infeasible](https://en.wikipedia.org/wiki/Game_complexity#Complexities_of_some_well-known_games), particularly as we add players and spaces. Fortunately, the state space of this game (or at least the 3-player, 10-space "base" version of it) is small enough to explore in under a second. What the `makeOptimalMove` script does is essentially the following:
  - Start with `N` players an empty board of size `M`
  - The first player considers her moves:
    - She starts by hypothetically placing her token at the first space
    - She calculates what her payout would be if the other `N - 1` players place their tokens in a way that maximizes their payout
      - She knows the other players will try each *available* space on the board as it exists after her hypothetical move
    - She continues down the line until she has considered all `M` spaces and found the one that yields the highest payout, and puts her token there
  - The next player considers her available moves on the board in its new state.
  - ...and so on and so forth!

## Numerical results

In the "standard" game, the program gave the following results:
```
Optimal first move is 5 with profit $21.00 (38.18% of the total money)
Average profit for non-first moves is $17.00
Advantage of moving first is $4.00
```
Player A put her token in the middle, player B put her token on 9, and player C put her token on 8. If player A had gone too low, the higher-position players would have gotten more money by proximity, and if player A had gone too high, another player would have placed her token just below player A's, stealing all of the lower-hanging fruits. The middle placement is, as they say, just right.

The "middle" strategy continued to win as the number of spaces increased from 10 (interestingly, when the number of spaces were 8 or 9, it was optimal to take the second-highest position first).
```
# 3 players, 12 spaces
Optimal first move is 6 with profit $32.00 (41.03% of the total money)
Average profit for non-first moves is $23.00
Advantage of moving first is $9.00

# 3 players, 30 spaces
Optimal first move is 15 with profit $200.00 (43.01% of the total money)
Average profit for non-first moves is $132.50
Advantage of moving first is $67.50

# 3 players, 60 spaces
Optimal first move is 31 with profit $840.50 (45.93% of the total money)
Average profit for non-first moves is $494.75
Advantage of moving first is $345.75
```
Now, I know what you're thinking: "Hey, that looks like it's monotonically increasing!" It does look that way, but it's actually just a coincidence. The advantage seems to top out and hover around 45%, or 12% more of the pot than a random move would get you. Not bad!

![Unimpressive spaces plot](UnimpressivePlot.png)

When the number of players increases, however, this advantage appeared to dry up slightly. I wasn't able to get super robust data on this point, because the simulations starting taking too long (the algorithm checks every possible game tree, after all). No matter what, though, the best strategy is to go low. More players up top sinks player A farther down the number line, and she gets less additional payout for going first. But as this crude plot of the *relative* advantage (above I was referring to absolute advantage) demonstrates, the numbers are not conclusive.

![Unimpressive spaces plot](playerPlot.png)

## Conclusion
Things I could have done better:
  1. The JavaScript code is insanely clunky, and doesn't scale up to extra players or different numbers of spaces.
  2. The C++ is unbearably slow at `N_players` > 4 and/or `N_spaces` > 100. This is because it checks every possible branch of the [game tree](https://en.wikipedia.org/wiki/Game_tree) instead of pruning branches by taking advantage of what it already knows a good strategy is.
  3. The C++ doesn't output in a machine-friendly format.
  4. The visualizations are kind of weak.

Things I learned:
  1. In a game in which the objective is to be farther away from other players, the middle is the optimal first move unless the number of players is almost equal to the number of spaces.  
  2. Using the results of HTML select menus as JavaScript variables is easy!
  3. When debugging a recursive algorithm, check that information is being passed correctly, both *downward* and *upward*.
