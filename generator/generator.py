class Generator:
    
    def __init__(self, content):
        self.raw_data = content
        self.__result = None
        
    @property
    def result(self):
        return self.__result

    def generate(self):
        self.__result = self.raw_data
