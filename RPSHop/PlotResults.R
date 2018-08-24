library(data.table)
library(ggplot2)

setwd("~/Documents/Code/Riddler/RPSHop/")

plotResults <- function(maxHoops, Ntrials) {
  filename <- paste0("rpsh_", maxHoops, "_", Ntrials, ".csv")
  cleanName <- paste0("rpsh_", maxHoops, "_", Ntrials, "_clean.csv")
  system(paste("sed 's/[{}]//g'", filename, ">", cleanName))
  results <- fread(cleanName, header = F,
                   colClasses = c("numeric"),
                   col.names = c("avgDuration"))

  results$minutes <- results$avgDuration / 60
  
  ggplot(results,
         aes(x = seq_along(results$minutes),
             y = results$minutes)) +
    geom_point() + 
    stat_smooth(aes(y = results$minutes), method = "lm", 
                formula = y ~ x + I(x^2), size = 1) +
    xlab("Number of hoops") + 
    ylab("Average duration in minutes") +
    geom_hline(yintercept = 30) + 
    geom_vline(xintercept = 59, size = 0.5) + 
    annotate("text", min(results$minutes), 30, vjust = -1, hjust = -0.2,
             label = "Class period") +
    annotate("text", min(results$minutes), 59, vjust = 16.5, hjust = -2.4,
             label = "A 59-hoop game usually fills this time") +
    ggtitle("The average game duration has a smooth relationship to the number of hoops")
  
}

plotResults(100, 50)


