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