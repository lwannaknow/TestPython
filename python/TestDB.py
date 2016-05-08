# coding=utf-8
__author__ = 'Jim'

import unittest

from testpyramid.models import data_operation


class TestDB(unittest.TestCase):
    def setUp(self):
        self.operation = data_operation

    def tearDown(self):
        data_operation.conn.close()
        self.operation = None

        # def testAdd(self):
        #     operation._add(g_id=1, price=1, g_name="goods", number=1)

        # def dbDelete(self):
        #     operation._delete(1)
        #
        # def testFind(self):
        #     row = operation._find(1)
        #     # print row[2]

        # def testFindAll(self):
        #     row_all = operation._find_all()
        #     print row_all

        # def test_count_change(self):
        #     row = operation._count_change(-1,1)
        #     # print row[2]

        # def testUpdate(self):
        #     operation._update(2, u"商品名", 2, 1)

        # def suite():

        # suite.addTest(testDB("testDelete")
        # suite.addTest(testDB("testFind"))
        # suite.addTest(testDB("testUpdate"))
        # return suite


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(TestDB("testAdd"))
    # suite.addTest(TestDB("dbDelete"))
    suite.addTest(TestDB("testFindAll"))
    # suite.addTest(TestDB("testUpdate"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# if __name__ == "__main__":
#     unittest.main()
