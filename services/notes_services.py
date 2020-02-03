"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This class is for notes services which is used for notes creation.
"""


from models.db_operations import Models
from auth.login_authentication import response

class NoteServices:
    """
    This class is for notes services which is used for notes creation.
    """

    def __init__(self):
        self.data_base_object = Models()

    def createnote(self,data,form_keys):
        """
        This function is used for creating notes of particular user.
        """
        if len(form_keys):
            self.data_base_object.user_insert(data,table_name='notes')
            res = response(success=True, message="Entry Created Successfully")
            return res
        else:
            res = response(message="unsuccessfull")
            return res

    def update(self,data,condition,form_keys):
        """
        This function is used for updating  notes of particular user.
        """
        if len(form_keys):
            self.data_base_object.updatee(data,condition)
            res = response(success=True, message="Data Updated Successfully")
            return res
        else:
            res = response(message="unsuccessfull")
            return res

    def readd(self,data):
        """
        This function is used for reading notes of particular user.
        """
        if data:
            self.data_base_object.read(data)
            res = response(success=True, message="Data reading done")
            return res
        else:
            res = response(message="unsuccessfull")
            return res

    def delete(self,data):
        """
        This function is used for deleting the data of particular user.
        """
        if data:
            self.data_base_object.delete(data)
            res = response(success=True, message="Data deleted Successfully")
            return res

        else:
            res = response( message="Data deletion unsuccessfull")
            return res

    def pin(self,data):
        """
        This function is used for reading the pinned data of particular user.
        """
        if self.data_base_object.read_pin(data):
            res = response(success=True, message="Pinned data reading done")
            return res
        else:
            res = response(success=True, message="Pinned data reading is unsuccessfull")
            return res

    def trash(self,data):
        """
        This function is used for reading the trash data of particular user.
        """
        if self.data_base_object.read_trash(data):
            res = response(success=True, message=" data reading done")
            return res
        else:
            res = response(success=True, message="data reading is unsuccessfull")
            return res

    def archive(self,data):
        """
        This function is used for reading the archived data of particular user.
        """
        if self.data_base_object.read_archive(data):
            res = response(success=True, message="data reading done")
            return res
        else:
            res = response(success=True, message=" data reading is unsuccessfull")
            return res




