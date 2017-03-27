# Hadoop_practice
Write a MapReduce program that creates an index of all words that can be find in the body of a forum post and node id they can be found in.

### Hadoop Sample Command
hadoop fs -ls

hadoop fs -put inputfile.txt

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper code/mapper.py  -reducer code/reducer.py -file code/mapper.py -file code/reducer.py  -input myinput/access_log -output joboutput

### Exercice
1. Create an index of all words that can be find in the body of a forum post and node id they can be found in.
2. Calculate the mean of sales for each weekday.
   1. Calculate the mean on reducer
   2. Calculate the intermediate sum with combiner to reduce traffic.

3. Combine the user info and forum post to show the user reputation in the post.
4. Course Project
   1. Data Set: 
      * forum_node.tsv - forum posts
      * forum_users.tsv - user info
   2. Questions:
      1. For each student what is the hour during which the student has posted the most posts.
