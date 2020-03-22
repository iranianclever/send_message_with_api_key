import requests
import json


class SendMessage:
    ''' sending message through api key '''

    def __init__(self):
        ''' initialization '''
        # path of file numbers
        self.__PATH = 'numbers.json'
        # api key
        self.__API_key = '2F79766A61495263422B4655626F773361447A566D68534C4E43615A44414C4A7737583856693334366E493D'
        # url from web service
        self.__URL = f'https://api.kavenegar.com/v1/{self.__API_key}/sms/send.json'

    def return_persons(self):
        ''' returns numbers of json file with dictionary format '''
        # container of persons
        persons = {}
        # check for exist file or no
        try:
            # reading file
            with open(self.__PATH) as f:
                # convert to string
                text = f.read()
                # if not empty, loads text to json format
                if text:
                    persons = json.loads(text)
        # if not exist, create file
        except FileNotFoundError:
            open(self.__PATH, 'w')
        return persons

    def add_number(self, name, number):
        ''' add number and name to list '''
        # read all list of numbers
        persons = self.return_persons()
        with open(self.__PATH, 'w') as f:
            # create new numbers
            persons[name] = number
            # convert to json format
            json_format = json.dumps(persons)
            # writing on file
            f.write(json_format)

    def remove_number(self, name):
        ''' remove a number from list '''
        # container of persons
        persons = self.return_persons()
        # status for removed or no
        is_removed = False
        # open file for check
        with open(self.__PATH, 'w') as f:
            # loop from container of persons with keys(name)
            for person_name in persons.keys():
                # check the name to match
                if person_name == name:
                    # remove person from list
                    del persons[name]
                    # status is true
                    is_removed = True
                    # convert list to json format
                    json_format = json.dumps(persons)
                    # write file
                    f.write(json_format)
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
        with open(self.__PATH, 'w') as f:
            # loop from container of persons with keys(name)
            for person_name in persons.keys():
                # check the name to match
                if person_name == name:
                    # modify person number from list
                    persons[name] = new_number
                    # status is true
                    is_modify = True
                    # convert list to json format
                    json_format = json.dumps(persons)
                    # write file
                    f.write(json_format)
                    # break looping
                    break
        return is_modify

    def send(self, message):
        ''' sending message '''
        # persons with dictionary format
        persons = self.return_persons()
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
                print('ارسال شد', name, response.status_code)
                # return True
            else:
                print('عدم ارسال', name, response.status_code)
                # return False


send_message = SendMessage()

send_message.add_number('Amirhossein', '09100000000')
send_message.add_number('Sara', '09100000001')

send_message.remove_number('Amirhossein')

status = send_message.modify_number('Sara', '09130000000')


# send_message.send("سلام امروز من با شما کار دارم تماس بگیرید")
