import requests
import json


class SendMessage:
    ''' sending message through api key '''

    def __init__(self):
        ''' initialization '''
        # path of file numbers
        self.__PATH = 'numbers.json'
        # Path of API Key
        self.__PATH_API = 'api'
        # api key
        self.API_key = self.get_api_key()
        # url from web service
        self.__URL = f'https://api.kavenegar.com/v1/{self.API_key}/sms/send.json'

    def get_api_key(self):
        """ get api key from file """
        api = ''
        # Check and open api file
        try:
            # Open file API
            with open(self.__PATH_API) as f:
                api = f.read()
        except FileNotFoundError:
            open(self.__PATH_API, 'w')

        # Check API key for return
        if api:
            return api
        return None

    def save_api_key(self, api):
        """ Get api key and save to file api """
        # Set new api key to file
        with open(self.__PATH_API, 'w') as f:
            f.write(api)
        # Get again api key and assign to main api
        self.API_key = self.get_api_key()
        # url from web service
        self.__URL = f'https://api.kavenegar.com/v1/{self.API_key}/sms/send.json'

    def return_persons(self):
        ''' returns numbers of json file with dictionary format '''
        # container of persons
        persons = {}
        # check for exist file or no
        try:
            # reading file
            with open(self.__PATH, encoding='utf-8') as f:
                # convert to string
                text = f.read()
                # if not empty, loads text to json format
                if text:
                    persons = json.loads(text, encoding='utf-8')
        # if not exist, create file
        except FileNotFoundError:
            open(self.__PATH, 'w', encoding='utf-8')
        return persons

    def add_number(self, name, number):
        ''' add number and name to list '''
        # read all list of numbers
        persons = self.return_persons()
        with open(self.__PATH, 'w', encoding='utf-8') as f:
            # create new numbers
            persons[name] = number
            # convert to json format
            json_format = json.dumps(
                persons, ensure_ascii=False).encode('utf-8')
            # writing on file
            f.write(json_format.decode())

    def remove_number(self, name):
        ''' remove a number from list '''
        # container of persons
        persons = self.return_persons()
        # status for removed or no
        is_removed = False
        # open file for check
        with open(self.__PATH, 'w', encoding='utf-8') as f:
            # loop from container of persons with keys(name)
            for person_name in persons.keys():
                # check the name to match
                if person_name == name:
                    # remove person from list
                    del persons[name]
                    # status is true
                    is_removed = True
                    # convert list to json format
                    json_format = json.dumps(
                        persons, ensure_ascii=False).encode('utf-8')
                    # write file
                    f.write(json_format.decode())
                    # break looping
                    break
        return is_removed

    def modify_number(self, name, new_number):
        ''' modify number of list '''
        # container of persons
        persons = self.return_persons()
        # status for modified or no
        is_modify = False
        # open file for check
        with open(self.__PATH, 'w', encoding='utf-8') as f:
            # loop from container of persons with keys(name)
            for person_name in persons.keys():
                # check the name to match
                if person_name == name:
                    # modify person number from list
                    persons[name] = new_number
                    # status is true
                    is_modify = True
                    # convert list to json format
                    json_format = json.dumps(
                        persons, ensure_ascii=False).encode('utf-8')
                    # write file
                    f.write(json_format.decode())
                    # break looping
                    break
        return is_modify

    def send(self, message):
        ''' sending message '''
        # persons with dictionary format
        persons = self.return_persons()
        # Holder status of sending message
        status = {}
        # sending message to the person
        for name, number in persons.items():
            # valid data for send to web service
            payload = {
                'receptor': number,
                'message': message
            }
            # send message
            response = requests.post(self.__URL, data=payload)
            # check message correctly
            if response.status_code == 200:
                status[name] = f'ارسال شد | کد وضعیت : {response.status_code}'
            else:
                status[name] = f'ارسال نشده | کد وضعیت : {response.status_code}'
        return status
