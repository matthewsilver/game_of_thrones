# game_of_thrones

###Overview
This code base builds an inverted index from a specified corpus of text.

###Data
For this data, there are documents from Project Gutenberg available <here>

###Setup
Setting up an EMR cluster on AWS is the easiest way to deploy this program. EMR contains Spark out of the box and scales without user configuration. If the end user would like to run this program on a lower cost, he or she can use a t2.micro AWS EC2 instance with the Ubuntu 18.04 OS. However, Spark is not automatically installed on this instance type, and it is necessary to follow instructions to manually install and set up Spark. 
