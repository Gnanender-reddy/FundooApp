from models.datamanagement import DataBaseMangament

class Note:

    def createnote(self,data,form_keys):
        responce_data = {'success': True, 'data': [], 'message': ""}
        data_base_object = DataBaseMangament()
        if len(form_keys):
            print(data['user_id'], "------------------>gnanen")
            data_base_object.create_entry(data)
            responce_data.update({'success': True, ' data': [], 'message': "Entry Created Successfully"})
            return responce_data

        else:
            responce_data.update({'success': False, 'data': [], 'message': "unsuccessfull"})
            return responce_data

    def update(self,data,form_keys):
        responce_data = {'success': True, 'data': [], 'message': ""}
        data_base_object = DataBaseMangament()
        if len(form_keys):
            data_base_object.update(data)
            responce_data.update({'success': True, 'data': [], 'message': "Data Updated Successfully"})
            return responce_data

        else:
            responce_data.update({'success': False, 'data': [], 'message': "unsuccessfull"})
            return responce_data

    def delete(self,data):
        data_base_object = DataBaseMangament()
        respon = {'success': True, 'data': [], 'message': ""}
        if id:

            data_base_object.delete(data)
            respon.update({'success': True, 'data': [], 'message': "Data deleted Successfully"})
            return respon

        else:
            respon.update({'success':False,'data':[],'message':'data deletion unsuccessfull'})
            return respon


