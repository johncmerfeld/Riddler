# NumberProfit

## The topline conclusion: The winning strategy is to be the lowest-placed token of the group; let the other players crowd out the high-value spaces while you sweep up many low-dollar ones.

## [The challenge](https://fivethirtyeight.com/features/step-1-game-theory-step-2-step-3-profit/)
From Steven Pratt, use your econ, win some cash:

Ariel, Beatrice and Cassandra — three brilliant game theorists — were bored at a game theory conference (shocking, we know) and devised the following game to pass the time. They drew a number line and placed $1 on the 1, $2 on the 2, $3 on the 3 and so on to $10 on the 10.

Each player has a personalized token. They take turns — Ariel first, Beatrice second and Cassandra third — placing their tokens on one of the money stacks (only one token is allowed per space). Once the tokens are all placed, each player gets to take every stack that her token is on or is closest to. If a stack is midway between two tokens, the players split that cash.

How will this game play out? How much is it worth to go first?

*A grab bag of extra credits:* What if the game were played not on a number line but on a clock, with values of $1 to $12? What if Desdemona, Eleanor and so on joined the original game? What if the tokens could be placed anywhere on the number line, not just the stacks?

## Workflow:
For starters, I thought it'd be fun to make a real, playable version of the game, which you can find [here](https://johncmerfeld.github.io/numberProfit.html). I messed around with this for a while and thought I knew what the optimal move for player A was (8), but it was hard to be sure without writing everything down. Therefore, it was time for some MiniMax game-tree traversal!

Getting the C++ code to compile didn't take long, but I struggled to actually achieve optimal gameplay. At first, I was fooled because the result confirmed my hunch that player A should place her token on space 8, with player B placing her token on 6, also as I thought was optimal. Then I noticed that player C was outfoxing A by placing her token on 9, putting A in last place!

I wondered momentarily whether that wasn't the point of the riddle; that the player who acts first is always at a disadvantage. But there *was* an optimal first placement for A that I found with a smaller experiment: 3 players and 5 spots. In that case, A should (counterintuitively, I thought) place her token on 3, collecting 1+2+3=6 dollars, the most possible.

Eventually, I found the bug in my code by which player A wasn't fully considering player C's possible moves, and the program got up and running properly!

## Numerical results
