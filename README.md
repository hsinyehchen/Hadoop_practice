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
      2. Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer.
      3. Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
      4. As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
