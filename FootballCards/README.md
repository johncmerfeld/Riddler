# FootballCards

### Topline conclusion: It takes 5 weeks on average to get every card in the Silver set, and 19 weeks on average to get every card in the Gold set. This was proven both theoretically and empirically.

## [The challenge](https://fivethirtyeight.com/features/id-like-to-use-my-riddler-lifeline/)

From Jerry Meyers, a conundrum timed to kick off the football season!

My son recently started collecting Riddler League football cards and informed me that he planned on acquiring every card in the set. It made me wonder, naturally, how much of his allowance he would have to spend in order to achieve his goal. His favorite set of cards is Riddler Silver; a set consisting of 100 cards, numbered 1 to 100. The cards are only sold in packs containing 10 random cards, without duplicates, with every card number having an equal chance of being in a pack.

Each pack can be purchased for $1. If his allowance is $10 a week, how long would we expect it to take before he has the entire set?

What if he decides to collect the more expansive Riddler Gold set, which has 300 different cards?

## Strategy

This one was thankfully quite simple! I decided to tackle it from both the theoretical and empirical angles. The theory goes like this:

- The first pack you buy gets you 10 new cards, guaranteed. 
- You can expect the second pack to net you 9 new cards and 1 duplicate, since you started with 10% of the total cards. 
- By the third set, you expect to have 19% of the total cards, so 81% of the cards you buy are expected to be new, getting you up to about 27. etc... 

I coded this up in R as the following formula:
```
cardsHas_i+1 = cardsHas_i + (cardsInDeck * ((cardsInSet - floor(cardsHas)) / 
                                             cardsInSet))
```
Note the use of the `floor()` function, a necessary discretization so that the function doesn't level off below 100. Without `floor()`, the formula would "punish" you for having expected fractions of cards, which isn't how it should work. i.e. it should only take you ten packs to get from 99 to 100 cards.

It's a recursive function, so I wrapped in a loop and let it go for `cardsInSet = 100` and `cardsInDeck = 10`. The answer was 50 packs (or **5 weeks of allowance**) for the Silver set and 186 packs (**19 weeks of allowance** for the Gold set. Note that even though the Gold set is only 3 times larger, it takes almost 4 times longer to get all the cards because of all the extra time spent just trying to get the last few new cards.

But if there's one thing that's stubbornly part of my brand, it's Monte Carlo simulations. Let's see what happens when we just "play the game."

The Python code actually draws ten unique cards at random from the set and adds them to a collection. It continues doing so until the collection is full. I found that for large numbers of trials (hundreds of thousands), the average number of Silver packs bought was... 50. Similarly, for the Gold set of 300 cards, the average number of packs bought was 186, in agreement with the theoretical result.  




