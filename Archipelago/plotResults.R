setwd("Documents/Code/Riddler/Archipelago/")
library(ggplot2)
library(data.table)

data <- fread("CommunitiesLeft.csv")

ggplot(data,
       aes(x = n,
           y = p,
           color = communities)) +
  geom_tile(aes(fill = communities),
            colour = "white") + 
  scale_fill_gradient(low = "white",
                      high = "darkblue") +
  xlab("Number of islands") +
  ylab("Probability of eruption") +
  labs(color = "Number of disjointed communities")
  ggtitle("")
 
