import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from zipfile import ZipFile,BadZipFile
from os.path import isfile
import os
class Test(unittest.TestCase):

    def check_zip_encryption_flags(self, zip_filepath):
        """
        Checks if individual members within a ZIP file are encrypted using flag_bits.
        Returns a list of (filename, is_encrypted) tuples.
        """
        encrypted_members = []
        try:
            with ZipFile(zip_filepath, 'r') as zf:
                for zinfo in zf.infolist():
                    # Check the encryption flag (0x1) in flag_bits
                    is_encrypted = bool(zinfo.flag_bits & 0x1)
                    encrypted_members.append((zinfo.filename, is_encrypted))
        except BadZipFile:
            print(f"Error: '{zip_filepath}' is not a valid ZIP file or is corrupted.")
        return encrypted_members

    @weight(1)
    @number("1")
    def test_zippwd(self):

        submission_path = os.path.join(os.getcwd(),"submission","hacker.zip")

        #Check if zip file exists
        self.assertTrue(isfile(submission_path), "Can not find file name \'hacker.zip\'")

        # All members in the zip file must be encrypted
        member_encryption_status = self.check_zip_encryption_flags(submission_path)
        for filename, is_encrypted in member_encryption_status:
            self.assertTrue(is_encrypted, "Zip file must be password protected")

        # Check if the password = hacker
        try:
            with ZipFile(submission_path) as zf:
                zf.extractall(path=os.path.join(os.getcwd(),"submission"), pwd='hacker'.encode('utf-8'))

        except Exception as e:
            self.assertTrue(False, e)




