library(ggplot2)

df <- data.frame(spaces = c(10, 12, 14, 17, 20, 24, 28, 34, 40, 50, 60, 75, 100),
                 advantage = c(38.18, 41.03, 42.86, 43.1, 43.33, 40, 46.8, 46.39, 46.1, 46.67, 45.93, 46.53, 45.78))

ggplot(df,
       aes(x = spaces,
           y = advantage)) + 
  geom_point() +
  geom_line() +
  xlim(0, 100) + 
  ylim(0, 50) + 
  ylab("Advantage (%)") +
  xlab("Available spaces") +
  ggtitle("Not much to see here!")


df2 <- data.frame(n_players = c(3, 4, 5, 6),
                  advantage = c(41.33, 31.43, 21.43, 19.29),
                  random = c(33.33, 25, 20, 16.67))
df2$gainPct <- (1 - (df2$random / df2$advantage)) * 100

ggplot(df2,
       aes(x = n_players,
           y = gainPct)) + 
  geom_point() +
  geom_line() +
  xlim(0, 7) + 
  ylim(0, 25) + 
  ylab("How much it pays to go first (%)") +
  xlab("Number of players") +
  ggtitle("More inconclusive evidence!")
