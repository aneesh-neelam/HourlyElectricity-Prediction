# Hourly Electricity Usage - Prediction

A simple MapReduce program that attempts to predict the hourly electricity usage

## Instructions

We shall be running this program using the Hadoop Streaming API

#### Place data into HDFS:
    $ hadoop fs -put ./data.csv [hdfs-path-to-input]

#### Run MapReduce program on Hadoop cluster:
    $ hadoop jar $HADOOP_PREFIX/share/hadoop/tools/lib/hadoop-*streaming*.jar -file [local-path-to-mapper] -mapper [local-path-to-mapper] -file [local-path-to-reducer] -reducer [local-path-to-reducer] -input [hdfs-path-to-input] -output [hdfs-path-to-output]

### Data Source
* K. Kalyani, [kkalyanims@gmail.com](mailto:kkalyanims@gmail.com), T. U. K. Arts College, Karanthai, Thanjavur

### References
* Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science
