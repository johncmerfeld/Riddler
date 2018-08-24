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
    xlab("Number of hoops") + 
    ylab("Average duration in minutes")
}

plotResults(40, 100)
