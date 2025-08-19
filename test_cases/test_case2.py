import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
import json
from os.path import isfile
import os
class Test(unittest.TestCase):

    @weight(1)
    @number("2")
    def test_json(self):

        json_file_path = os.path.join(os.getcwd(),"submission","hacker.json")

        self.assertTrue(isfile(json_file_path), "Autograder can not find file name \'hacker.json\'. This might be due to an issue during decompression, or because the file was placed in a folder before compression.")
        try:
            with open(json_file_path, 'r',  encoding='utf-8') as json_data:
                json_content = json.load(json_data)
                json_data.close()
        except Exception as e:
            self.assertTrue(False, "Error occurs when loading json content: "+ str(e))

        self.assertTrue(("legal_name" in json_content or "名字" in json_content ), "Cannot find key named \'legal_name\' or \'名字\'")
        self.assertTrue(("handle" in json_content or "网名" in json_content ), "Cannot find key named \'handle\' or \'网名\'")
        self.assertTrue(("email" in json_content or "邮件" in json_content ), "Cannot find key named \'email\' or \'邮件\'")
        self.assertTrue(("asu_id" in json_content or "ASU_ID" in json_content ), "Cannot find key named \'asu_id\' or \'ASU_ID\'")
        self.assertTrue(("concerns" in json_content or "期待与担心" in json_content ), "Cannot find key named \'concerns\' or \'期待与担心\'")

        print(json_content)




