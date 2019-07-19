import re
import boto
from pyspark.context import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import udf

class InvertedDictionary():
    def __init__(self, fileConfig):
        self.sc = SparkContext()
        self.sqlContext = HiveContext(self.sc)
        self.invertedDict = {}
        self.conn = boto.connect_s3(host='s3.amazonaws.com')
        self.bucket = fileConfig['s3_bucket']
        self.folder = fileConfig['s3_folder']

    def buildInvertedDict(self):
        bucket = self.conn.get_bucket(self.bucket)
        for idx, file in enumerate(bucket.list(self.folder, '/')):
            if idx == 0:
                continue
            fileId = file.key.split('/')[1]
            rdd = self.sc.textFile('s3a://{}/{}/{}'.format(self.bucket, self.folder, fileId))
            output = rdd.flatMap(lambda (words): [(re.sub(r'[^a-z\']', '', word)) for word in words.lower().split()])\
                  .map(lambda (word): (word, fileId))
         
            for row in output.collect():
                word, docId = str(row[0]), int(row[1])
                if word not in self.invertedDict:
                    self.invertedDict[word] = [docId]
                else:
                    if docId in self.invertedDict[word]:
                        pass
                    else:
                        self.invertedDict[word].append(docId)

def main():
    fileConfig = {
        's3_bucket': 'mattsilver-insight',
        's3_folder': 'game-of-thrones/'
    }
    id = InvertedDictionary(fileConfig)
    id.buildInvertedDict()
    print(id.invertedDict)

if __name__ == '__main__':
    main()
