setwd("Documents/Code/Riddler/SultanSuitors/")
library(ggplot2)
library(data.table)

data <- fread("CommunitiesLeft.csv")
data$communitiesFraction <- data$communities / data$n

print(mean(data$communitiesFraction))
# [1] 0.178979
print(median(data$communitiesFraction))
# [1] 0.1983696

ggplot(data,
       aes(x = n,
           y = p,
           color = data$communities)) +
  geom_tile(aes(fill = data$communities),
            colour = "white") + 
  scale_fill_gradient(low = "white",
                      high = "darkblue") +
  xlab("Number of islands") +
  ylab("Probability of eruption") +
  ggtitle("An eruption probability of 0.5 destroys maximal bridges without decimating too many islands")

