'''
Basic example showing how to read and validate data from a file using Pydantic.
https://github.com/ArjanCodes/2021-pydantic/blob/main/example.py
'''

''' pydantic can generate json schema  
    easily read config files
    '''



import json
import pydantic 
from typing import Optional, List

class ISBN10FormatError(Exception):
    ''' custom error that is raised when ISBN10 doesnt have the right format'''

    def __init__(self, values: str, message: str) -> None:
        self.values = values
        self.message = message
        super.__init__(message)


class ISBBMissingError(Exception):
    ''' custom error that is raised when both ISBN13 and ISBN10 are missing'''
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super.__init__(message)

class Author(pydantic.BaseModel):
    name: str
    verified: bool


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float 
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    author2: Optional[Author]


    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        ''' make sure there is either an isbn10 or isbn 13'''
        if "isbn_10" not in values and "isbn13" not in values:
            raise ISBBMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13"
            )
        return  values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        chars = [c for c in value if c in "0123456789Xx" ]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        
        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value 


    class Config:
        '''pydantic config class'''
        allow_mutation = False
        anystr_lower = True


def main() -> None:
    ''' main function '''

    # read data from a json file
    with open('./data.json') as file:
        data = json.load(file)
        books: List[Book] = [ Book(**item) for item in data]
        #print(books[0].dict())
        print(books[0].dict(exclude={"price"})) # print all fields except price
        #print(bools[0].copy())
        #print(books[0].dict(include={"price"}))  # include price only



if __name__ == "__main__":
    main()