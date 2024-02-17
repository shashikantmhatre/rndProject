from datetime import datetime
from language.context.DataType import DataType


class Data:

    def __init__(self, value, alias:str=None, datatype=None):
        self.value = value
        self.alias = alias
        if datatype is None:
            if value is None:
                self.datatype = DataType.NONE
            elif isinstance(value, int):
                self.datatype = DataType.INT
            elif isinstance(value, float):
                self.datatype = DataType.INT
            elif isinstance(value, datetime):
                self.datatype = DataType.DATE
            elif isinstance(value, list):
                self.datatype = DataType.LIST
            else:
                self.datatype = DataType.OBJECT
        else:
            self.datatype = datatype

    def gettype(self) -> DataType:
        return self.datatype

    def getalias(self) -> str:
        return self.alias

    def getvalue(self):
        return self.value

    def __str__(self):
        return f'Data ( value = {self.value}, alias = {self.alias}, datatype = {self.datatype}'
