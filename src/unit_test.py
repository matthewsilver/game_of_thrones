from build_inverted_index import InvertedDictionary

class TestClass:
    def __init__(self):
        pass

    def test_buildInvertedDict(self):
        fileConfigTest = {
            's3_bucket': 'mattsilver-insight',
            's3_folder': 'got_test/'
        }
        id = InvertedDictionary(fileConfigTest)
        id.buildInvertedDict()
        invDict = {
            'a': [0], 'word': [0], 'another': [1], 'for': [0], 'this': [0],
            'is': [0, 1], 'there': [1], 'it': [0], 'here': [1], 'file': [0, 1],
            'test': [0], 'counts': [0]}
        assert(id.invertedDict == invDict)

def main():
    t = TestClass()
    t.test_buildInvertedDict()

if __name__ == '__main__':
    main()
