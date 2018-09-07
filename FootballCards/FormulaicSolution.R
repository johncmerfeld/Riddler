howManyPacks <- function(cardsInSet, cardsInDeck) {

  # initialize cardsHas, the 'Y value' of the function
  cardsHas <- 0
  # initialize packsBought, the 'X value' of the function
  packsBought <- 0
  
  # store results in a progress vector (in case we want to plot it)
  progress <- c()
  
  while (cardsHas < cardsInSet) {
    packsBought <- packsBought + 1
    # the floor function ensures that we're not 'penalized' for cards we don't actually have yet.
    cardsHas <- cardsHas + (cardsInDeck * ((cardsInSet - floors(cardsHas)) / 
                                             cardsInSet))
    progress[packsBought] <- cardsHas
  }
  return(progress)
}



