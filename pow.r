library(dplyr)
library(assertr)

pow <- function(number) {
    return(strtoi(number) * strtoi(number))
}

tests = data.frame(x = 1:10)
tests["y"] = lapply(tests["x"], pow)

print(tests)

tests %>% 
    assert(in_set(1,4,9,16,25,36,49,64,81,99), y)