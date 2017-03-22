# Hadoop_practice
Write a MapReduce program that creates an index of all words that can be find in the body of a forum post and node id they can be found in.

### Hadoop Sample Command
hadoop fs -ls

hadoop fs -put inputfile.txt

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper code/mapper.py  -reducer code/reducer.py -file code/mapper.py -file code/reducer.py  -input myinput/access_log -output joboutput

### Exercice
1. Create an index of all words that can be find in the body of a forum post and node id they can be found in.
2. Calculate the mean of sales for each weekday.
  * Calculate the mean with reducer
  * Calculate the intermediate sum and counts on mapper 
