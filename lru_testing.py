from lru import *
import unittest

class lruTest(unittest.TestCase):

    def _init_(self):
        pass

    def testcases(self):
        obj = lru(3)
        assert obj.put(1,"one")=="done"
        assert obj.put(2,"two")=="done"
        assert obj.put(3,"three")=="done"
        assert obj.get(1)=="one"
        assert obj.get(1)=="one"
        assert obj.put(4,"four")=="done"
        assert obj.put(5,"five")=="done"
        assert obj.get_cache()== {1:'one', 4:'four', 5:'five'}
        print ("Test Cases Passed Successfully")    

if __name__ == '__main__':
    unittest.main()

