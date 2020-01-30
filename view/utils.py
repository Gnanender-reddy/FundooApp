import re
class Utility:

    def email_validation(self, email):
        """
        This function is used for checking whether entered email is in correct format or not.
        """
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex, email):
            return True
        else:
            return False


    def validate_file_extension(self, data):
            import os
            ext = os.path.splitext(data['profile_path'])[1]  # [0] returns path+filename
            valid_extensions = ['.jpg']
            if not ext.lower() in valid_extensions:
                print("Unsupported file extension.")
            else:
                return True
                # raise ValidationError(u'Unsupported file extension.')

    def validate_file_size(self, data):
            filesize = len(data['profile_path'])
            if filesize > 10485760:
                print("The maximum file size that can be uploaded is 10MB")
            else:
                return True

    def password_validation(self, data):
        """
         This function is used to checking whether password and confirm password are same.
        """
        if data['password'] == data['confirmpassword']:
            return True
        else:
            return False
