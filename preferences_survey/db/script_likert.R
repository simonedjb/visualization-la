library("likert")

evaluation_db = read.csv("/home/andre/Dropbox/Backup/Documentos/Doutorado/Pesquisa/Interview Visualization/preferences_survey/db/z_instructors_evaluation.csv", comment.char="#", header = TRUE, check.names = FALSE)

v01_charts<-c('VG-01 (a)','VG-01 (b)','VG-01 (c)','VG-01 (d)','VG-01 (e)','VG-01 (f)','VG-01 (g)','VG-01 (h)','VG-01 (i)','VG-01 (j)','VG-01 (k)','VG-01 (l)')
v02_charts<-c('VG-02 (a)','VG-02 (b)','VG-02 (c)','VG-02 (d)','VG-02 (e)','VG-02 (f)','VG-02 (g)','VG-02 (h)','VG-02 (i)','VG-02 (j)')
v03_charts<-c('VG-03 (a)','VG-03 (b)','VG-03 (c)','VG-03 (d)','VG-03 (e)','VG-03 (f)','VG-03 (g)')
v04_charts<-c('VG-04 (a)','VG-04 (b)','VG-04 (c)','VG-04 (d)','VG-04 (e)','VG-04 (f)','VG-04 (g)','VG-04 (h)','VG-04 (i)','VG-04 (j)')
v05_charts<-c('VG-05 (a)','VG-05 (b)','VG-05 (c)','VG-05 (d)','VG-05 (e)','VG-05 (f)')
v06_charts<-c('VG-06 (a)','VG-06 (b)','VG-06 (c)','VG-06 (d)')
v07_charts<-c('VG-07 (a)','VG-07 (b)','VG-07 (c)','VG-07 (d)')
v08_charts<-c('VG-08 (a)','VG-08 (b)','VG-08 (c)','VG-08 (d)','VG-08 (e)')
v09_charts<-c('VG-09 (a)','VG-09 (b)','VG-09 (c)','VG-09 (d)')
v10_charts<-c('VG-10 (a)','VG-10 (b)','VG-10 (c)','VG-10 (d)','VG-10 (e)','VG-10 (f)','VG-10 (g)','VG-10 (h)','VG-10 (i)','VG-10 (j)','VG-10 (k)','VG-10 (l)','VG-10 (m)')
v11_charts<-c('VG-11 (a)','VG-11 (b)','VG-11 (c)','VG-11 (d)','VG-11 (e)')
charts<-c('VG-01 (a)','VG-01 (b)','VG-01 (c)','VG-01 (d)','VG-01 (e)','VG-01 (f)','VG-01 (g)','VG-01 (h)','VG-01 (i)','VG-01 (j)','VG-01 (k)','VG-01 (l)', 'VG-02 (a)','VG-02 (b)','VG-02 (c)','VG-02 (d)','VG-02 (e)','VG-02 (f)','VG-02 (g)','VG-02 (h)','VG-02 (i)','VG-02 (j)', 'VG-03 (a)','VG-03 (b)','VG-03 (c)','VG-03 (d)','VG-03 (e)','VG-03 (f)','VG-03 (g)', 'VG-04 (a)','VG-04 (b)','VG-04 (c)','VG-04 (d)','VG-04 (e)','VG-04 (f)','VG-04 (g)','VG-04 (h)','VG-04 (i)','VG-04 (j)', 'VG-05 (a)','VG-05 (b)','VG-05 (c)','VG-05 (d)','VG-05 (e)','VG-05 (f)', 'VG-06 (a)','VG-06 (b)','VG-06 (c)','VG-06 (d)', 'VG-07 (a)','VG-07 (b)','VG-07 (c)','VG-07 (d)', 'VG-08 (a)','VG-08 (b)','VG-08 (c)','VG-08 (d)','VG-08 (e)', 'VG-09 (a)','VG-09 (b)','VG-09 (c)','VG-09 (d)', 'VG-10 (a)','VG-10 (b)','VG-10 (c)','VG-10 (d)','VG-10 (e)','VG-10 (f)','VG-10 (g)','VG-10 (h)','VG-10 (i)','VG-10 (j)','VG-10 (k)','VG-10 (l)','VG-10 (m)', 'VG-11 (a)','VG-11 (b)','VG-11 (c)','VG-11 (d)','VG-11 (e)')

results_v01 <- evaluation_db[, names(evaluation_db)[c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)]]
results_v02 <- evaluation_db[, names(evaluation_db)[c(14, 15, 16, 17, 18, 19, 20, 21, 22, 23)]]
results_v03 <- evaluation_db[, names(evaluation_db)[c(24, 25, 26, 27, 28, 29, 30)]]
results_v04 <- evaluation_db[, names(evaluation_db)[c(31, 32, 33, 34, 35, 36, 37, 38, 39, 40)]]
results_v05 <- evaluation_db[, names(evaluation_db)[c(41, 42, 43, 44, 45, 46)]]
results_v06 <- evaluation_db[, names(evaluation_db)[c(47, 48, 49, 50)]]
results_v07 <- evaluation_db[, names(evaluation_db)[c(51, 52, 53, 54)]]
results_v08 <- evaluation_db[, names(evaluation_db)[c(55, 56, 57, 58, 59)]]
results_v09 <- evaluation_db[, names(evaluation_db)[c(60, 61, 62, 63)]]
results_v10 <- evaluation_db[, names(evaluation_db)[c(64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76)]]
results_v11 <- evaluation_db[, names(evaluation_db)[c(77, 78, 79, 80, 81)]]
results <- evaluation_db[, names(evaluation_db)[c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81)]]


results_geral <- change_levels(results_v01, v01_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v01_charts)

results_geral <- change_levels(results_v02, v02_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v02_charts)

results_geral <- change_levels(results_v03, v03_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v03_charts)

results_geral <- change_levels(results_v04, v04_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v04_charts)

results_geral <- change_levels(results_v05, v05_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v05_charts)

results_geral <- change_levels(results_v06, v06_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v06_charts)

results_geral <- change_levels(results_v07, v07_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v07_charts)

results_geral <- change_levels(results_v08, v08_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v08_charts)

results_geral <- change_levels(results_v09, v09_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v09_charts)

results_geral <- change_levels(results_v10, v10_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v10_charts)

results_geral <- change_levels(results_v11, v11_charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = v11_charts)

results_geral <- change_levels(results, charts)
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = charts)

change_levels <- function(df, colnames){
  for(i in  1:length(colnames)){
    colname <- colnames[i]
    df[,colname] <- factor(df[,colname], 
                           levels = c('strong disagree','partially disagree','slightly disagree','neutral','slightly agree','partially agree','strong agree'), ordered = TRUE)
  }
  return(df)
}


scale_height = knitr::opts_chunk$get('fig.height')*5
scale_width = knitr::opts_chunk$get('fig.width')*5
knitr::opts_chunk$set(fig.height = scale_height, fig.width = scale_width)

theme_update(legend.text = element_text(size = rel(0.5)))
plot(likert(results_geral),type="bar",ordered=FALSE, group.order = charts)