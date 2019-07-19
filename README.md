# game_of_thrones

### Overview
This code base builds an inverted index from a specified corpus of text. An inverted index is a key/value mapping where keys are words and values the documents the word appears in. For example, if we have two documents as shown:

__Document 1__
```
Everything is fine.
```

__Document 2__
```
Everything is on fire.
```

Then the resulting inverted index is
```
{
  'everything': [1,2],
  'is': [1,2],
  'fine': [1],
  'on': [2],
  'fire': [2]
}
```

### Data
The text documents used for this code base are from the Project Gutenberg text corpi. They can be found [here](https://github.com/Samariya57/coding_challenges/tree/master/data/indexing).

### Setup
Setting up an EMR cluster on AWS is the easiest way to deploy this program. EMR contains Spark out of the box and scales without user configuration. If the end user would like to run this program on a lower cost, he or she can use a t2.micro AWS EC2 instance with the Ubuntu 18.04 OS. However, Spark is not automatically installed on this instance type, and it is necessary to follow instructions to manually install and set up Spark. 

If you use EMR, a small amount of nodes (1 master, 2 workers) of size m3.xlarge should be sufficient for tens of megabytes of text. For larger numbers and sizes of documents, larger instances and/or more workers should be experimented with.

### Input Files

Place all of the documents you would like in the inverted index in S3, under the same bucket and folder. Name each file a number incrementing from 0. For example, if you have 3 documents, they should be named '0', '1', and '2' (no extensions in the name).

### Running the Code
Clone this repo, navigate to `src`, and run `build_inverted_index.py`. By default, the inverted index is printed to output, but you can redirect the output to a file if you would like to pickle it and save it for later.

### Testing
There is a unit test under `src` called `unit_tests.py` which contains a class under which tests can be created and run. The current test verifies that an inverted index built from two very small documents is correct. I tried implementing pytest but ran into issues getting it to run on pyspark; with more time, I could figure out how to properly implement this for a more robust testing framework. 
