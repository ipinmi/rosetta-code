# 100 doors 
doors_puzzle <- function(ndoors=100, passes=100) {
  #FALSE = CLOSED , TRUE=OPENED
  #All doors are closed at first 
  doors <- rep(FALSE, ndoors)
  
  for (x in seq(1, passes)) {
    # the x is the current pass number and it is used to pick eac xth door and
    # toggle it 
    multiples_in_passes <- seq(0, ndoors, x) 
    doors[multiples_in_passes] <- !doors[multiples_in_passes]
  }
  
  return (which(doors == TRUE))
}

doors_puzzle()
