import unittest
import sys
sys.path.append('../util')
from test_get_post import Runmain

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("类执行之前的方法")
        pass

    @classmethod
    def tearDownClass(cls):
        # print("类执行之后的方法")
        pass

    #每次方法前执行
    def setUp(self):
        self.run = Runmain()

    #每次方法后执行
    def tearDown(self):
        pass

    def test_01(self):
        url = 'https://as-test.topchitu.com/api/after/task/task-list.shtml'
        headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                   "content-type": "application/x-www-form-urlencoded"}
        data={
            "taskTypeId":"1408",
            "taskStatusId":"5392",
            "sortBy":"SORT_BY_CREATED_TIME_DESC",
            "dateField":"CREATED_TIME",
            "exportType":"AFTERTASK",
            "taskPattern":"DETAIL",
            "assigneeType":"taskType",
            "page":"0",
            "pageSize":"20",
            "checkedTab":"CREATED",
            "createdStatusId":"5392",
            "taskStep":"CREATED",
            "deleteAssignee":"true",
            "size":"20",
            "taskStatusIds":"5392"
        }
        res = self.run.run_main(url,None,data,headers=headers,method='GET')
        # print(res)
        # print(type(res['content'][0]["userId"]))
        self.assertEqual(res['content'][0]["userId"], 100727373, '返回状态错误，不为200')
        # self.assertEqual(res.get("code"), 200, '返回状态错误，不为200')
        # self.assertEqual(res['value']['name'],'so')
        print("这是第一个测试方法")

    @unittest.skip("无条件跳过此用例")
    def test_02(self):
        url = 'http://www.tuling123.com/openapi/api'
        params = {
            "taskTypeId": "1408",
            "taskStatusId": "5392",
            "sortBy": "SORT_BY_CREATED_TIME_DESC",
            "dateField": "CREATED_TIME",
            "exportType": "AFTERTASK",
            "taskPattern": "DETAIL",
            "assigneeType": "taskType",
            "page": "0",
            "pageSize": "20",
            "checkedTab": "CREATED",
            "createdStatusId": "5392",
            "taskStep": "CREATED",
            "deleteAssignee": "true",
            "size": "20",
            "taskStatusIds": "5392"
        }
        res = self.run.run_main(url,params,None,None,'GET')
        print(res)
        self.assertEqual(res['code'], '200', '返回状态错误，不为200')
        print("这是第二个测试方法")