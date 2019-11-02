setwd("Riddler/SultanSuitors/")
library(ggplot2)
library(data.table)

data <- fread("SuitorData.csv")
data <- data[data$n_trials == 100000]

ggplot(data,
       aes(x = w,
           y = abs(10 - avg_rank) - 4.49,
           fill = data$avg_rank)) +
  geom_bar(stat = "identity") +
  scale_fill_continuous(name = "Expected rank", low = "blue", high = "black") +
  xlab("How many suitors to ignore before picking") +
  ylab("Number of ranks better than random (5.5) the expected suitor is") +
  ggtitle("Ignoring the first two suitors maximses the expected suitor quality") +
  scale_x_continuous(breaks = 0:9, labels = data$w)


ggplot(data,
       aes(x = w,
           y = pct_wins,
           fill = data$pct_wins)) +
  geom_bar(stat = "identity") +
  scale_fill_continuous(name = "Likelihood (%)", low = "black", high = "red") +
  xlab("How many suitors to ignore before picking") +
  ylab("Percentage of the time the absolute best suitor is picked") +
  ggtitle("Ignoring the first four suitors maximizes the odds of finding the absolute best one") +
  scale_x_continuous(breaks = 0:9, labels = data$w)


ggplot(data,
       aes(x = w,
           y = pct_losses,
           fill = data$pct_losses)) +
  geom_bar(stat = "identity") +
  scale_fill_continuous(name = "Likelihood (%)", low = "green", high = "black") +
  xlab("How many suitors to ignore before picking") +
  ylab("Percentage of the time the absolute worst suitor is picked") +
  ggtitle("To avoid picking the worst suitor, ignore the first one and then start looking") +
  scale_x_continuous(breaks = 0:9, labels = data$w)

