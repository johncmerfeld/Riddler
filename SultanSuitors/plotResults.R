setwd("Riddler/SultanSuitors/")
library(ggplot2)
library(data.table)

data <- fread("SuitorData.csv")
data <- data[data$n_trials == 100000]

ggplot(data,
       aes(x = w,
           y = abs(10 - avg_rank),
           fill = data$avg_rank)) +
  geom_bar(stat = "identity") +
  scale_fill_continuous(name = "abs(10 - average rank)", low = "blue", high = "black") +
  xlab("How many suitors to ignore before picking") +
  ylab("Expected suitor quality") +
  ggtitle("Ignoring the first two suitors maximses the expected suitor quality")

