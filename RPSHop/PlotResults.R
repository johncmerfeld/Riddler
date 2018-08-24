library(data.table)
library(ggplot2)

setwd("~/Documents/Code/Riddler/RPSHop/")

plotResults <- function(maxHoops, Ntrials) {
  system(paste("python RockPaperScissorsHop.py", maxHoops, Ntrials))
  filename <- paste0("rpsh_", maxHoops, "_", Ntrials, ".csv")
  results <- fread(filename, header = F,
                   colClasses = c("numeric"),
                   col.names = c("avgDuration"))
  
  ggplot(results,
         aes(x = seq_along(results$avgDuration),
             y = results$avgDuration)) +
    geom_point()
  
  return(results)
}

r <- plotResults(10, 10)
