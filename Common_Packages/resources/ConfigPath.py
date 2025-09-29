import os
import time

'''
This class is defined to set path of different types of file that needs to be uploaded in various steps
'''


class UploadFile:

    @staticmethod
    def file_upload_path(file_name):
        currentDirectory = os.path.dirname(__file__)
        img_file = f'\\{file_name}'
        path = currentDirectory + img_file
        return path



    @staticmethod
    def upload_pdf():
     currentDirectory = os.path.dirname(__file__)
     pdf_file= '\\resume_dummy.pdf'
     path_manual = currentDirectory+pdf_file
     return path_manual

    @staticmethod
    def upload_zip():
        currentDirectory = os.path.dirname(__file__)
        img_file = '\\bulk_upload.zip'
        path = currentDirectory + img_file
        return path

    @staticmethod
    def upload_xls():
        currentDirectory = os.path.dirname(__file__)
        img_file = '\\Data_File.xlsx'
        path = currentDirectory + img_file
        return path

    @staticmethod
    def upload_Qbank():
        currentDirectory = os.path.dirname(__file__)
        excel_file = '\\question_bank_bulk_upload.xlsx'
        path = currentDirectory + excel_file
        return path

    @staticmethod
    def upload_DiscussionFile():
        currentDirectory = os.path.dirname(__file__)
        img_file = '\\DiscussionFile.jpg'
        path = currentDirectory + img_file
        return path

    @staticmethod
    def upload_UsersFile():
        currentDirectory = os.path.dirname(__file__)
        img_file = '\\StaffBulk_Upload.xlsx'
        path = currentDirectory + img_file
        return path

    @staticmethod
    def upload_InteractionFile():
        currentDirectory = os.path.dirname(__file__)
        img_file = '\\InteractionFile.jpg'

        path = currentDirectory + img_file

        return path

    @staticmethod
    def upload_ReadingFile():
        currentDirectory = os.path.dirname(__file__)

        pdf_file = '\\ReadingFile.pdf'

        path_manual = currentDirectory + pdf_file
        return path_manual

    @staticmethod
    def upload_VideoFile():
        currentDirectory = os.path.dirname(__file__)
        vid_file = '\\Video.mp4'

        path = currentDirectory + vid_file

        return path

    @staticmethod
    def upload_VideoTranscript():
        currentDirectory = os.path.dirname(__file__)
        srt_file = '\\Video.srt'

        path = currentDirectory + srt_file

        return path



    @staticmethod
    def upload_StudentConnectFile():
        currentDirectory = os.path.dirname(__file__)
        img_file = '\\StudentConnectFile.jpg'
        path = currentDirectory + img_file
        return path


