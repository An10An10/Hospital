class Patient:
    def __init__(self, age, firstname, surname, diagnose, id, phone_number, status, address):
        self.set_firstname(firstname)
        self.set_surname(surname)
        self.set_age(age)
        self.set_diagnose(diagnose)
        self.set_status(status)
        self.__id = id
        self.__phone_number = phone_number
        self.__address = address

    def get_firstname(self):
        return self.__firstname

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__id

    def get_diagnose(self):
        return self.__diagnose

    def get_phone_number(self):
        return self.__phone_number

    def get_status(self):
        return self.__status

    def get_address(self):
        return self.__address

    def set_firstname(self, firstname):
        if isinstance(firstname, str):
            self.__firstname = firstname
        else:
            return 0

    def set_surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            return 0

    def set_age(self, age):
        if isinstance(age, int):
            if 0 < age <= 110:
                self.__age = age
            else:
                return 0
        else:
            return 0

    def set_diagnose(self, diagnose):
        if isinstance(diagnose, str):
            self.__diagnose = diagnose
        else:
            return 0

    def set_status(self, status):
        if isinstance(status, str):
            self.__status = status
        else:
            return 0

    def birthday(self):
        self.set_age(self.get_age() + 1)

