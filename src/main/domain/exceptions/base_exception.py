class ApplicationException(Exception):
    def __init__(self, phone, *args):
        self.phone = phone
        super().__init__(*args)
