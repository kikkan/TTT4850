options(error=recover)
# options(error=NULL)

d = read.delim("./data/data-315297-2023-02-15-1118-utf.txt", header=T)

## Reformat dumb shit
formatTime <- function(t) {
  tSplit = strsplit(t, ' ')[[1]]
  s=0
  for (i in seq(1, length(tSplit), 2)){
    s = s + switch(
      tSplit[i+1],
      "dager" = as.numeric(tSplit[i])*24*3600,
      "dag" = as.numeric(tSplit[i])*24*3600,
      "timer" = as.numeric(tSplit[i])*3600,
      "time" = as.numeric(tSplit[i])*3600,
      "minutt" = as.numeric(tSplit[i])*60,
      "minutter" = as.numeric(tSplit[i])*60,
      "sekunder" = as.numeric(tSplit[i]),
      "sekund" = as.numeric(tSplit[i]),
      0
    )
  }
  return(s)
}

# new.function <- function(a) {
#    for(i in 1:a) {
#       b <- i^2
#       print(b)
#    }
# }

times = d$Svartid
times

ftimes = lapply(times, formatTime)

cbind(times, ftimes)
