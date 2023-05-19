class IO_DATA(object):
    def __init__(self, reqest:str, response:str, status:bool)->None:
        self.request = reqest
        self.response = response
        self.status = status