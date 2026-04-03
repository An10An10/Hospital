from datetime import date

class Person:
    def __init__(self, n, s, db, a):
        self.set_name(n)
        self.set_surname(s)
        self.set_date_birthday(db)
        self.set_address(a)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_date_birthday(self):
        return self.__date_birthday

    def get_address(self):
        return self.__address

    def set_name(self, n):
        if isinstance(n, str) and n.strip():
            self.__name = n.strip()

    def set_surname(self, s):
        if isinstance(s, str) and s.strip():
            self.__surname = s.strip()

    def set_date_birthday(self, db):
        if isinstance(db, tuple) and len(db) == 3:
            d, m, y = db
            if 1 <= d <= 31 and 1 <= m <= 12 and 1900 <= y <= 2026:
                self.__date_birthday = db

    def set_address(self, a):
        if isinstance(a, str) and a.strip():
            self.__address = a.strip()

    def get_age(self):
        if not hasattr(self, '_Person__date_birthday'):
            
        today = date.today()
        d, m, y = self.__date_birthday
        age = today.year - y
        if (today.month, today.day) < (m, d):
            age -= 1
        return age

    def birthday(self):
        if hasattr(self, '_Person__date_birthday'):
            d, m, y = self.__date_birthday
            self.set_date_birthday((d, m, y + 1))

class Medic(Person):
    def __init__(self, n, s, db, a, q, nc, lp=None):
        super().__init__(n, s, db, a)
        self.set_quality(q)
        self.set_num_cab(nc)
        self.set_list_patient(lp if lp is not None else [])

    def get_quality(self):
        return self.__quality

    def get_num_cab(self):
        return self.__num_cab

    def get_list_patient(self):
        return self.__list_patient.copy() if self.__list_patient else []

    def set_quality(self, q):
        if isinstance(q, str) and q.strip():
            self.__quality = q.strip()

    def set_num_cab(self, nc):
        if isinstance(nc, int) and 1 <= nc <= 100:
            self.__num_cab = nc

    def set_list_patient(self, lp):
        if isinstance(lp, list):
            self.__list_patient = lp

    def add_patient(self, p):
        if isinstance(p, Patient):
            if p not in self.__list_patient:
                self.__list_patient.append(p)
                p.set_link_doctor(self)

    def remove_patient(self, p):
        if p in self.__list_patient:
            self.__list_patient.remove(p)
            if p.get_link_doctor() == self:
                p.set_link_doctor(None)
            

class Patient(Person):
    def __init__(self, n, s, db, a, d, st, ld=None):
        super().__init__(n, s, db, a)
        self.set_diagnose(d)
        self.set_status(st)
        self.set_link_doctor(ld)
        self.__id = id(self)
        self.__phone_number = None
        self.set_phone_number("")

    def get_id(self):
        return self.__id

    def get_phone_number(self):
        return self.__phone_number

    def get_diagnose(self):
        return self.__diagnose

    def get_status(self):
        return self.__status

    def get_link_doctor(self):
        return self.__link_doctor

    def set_phone_number(self, ph):
        if isinstance(ph, str):
            self.__phone_number = ph

    def set_diagnose(self, d):
        if isinstance(d, str) and d.strip():
            self.__diagnose = d.strip()

    def set_status(self, st):
        if isinstance(st, int) and 0 <= st <= 5:
            self.__status = st

    def set_link_doctor(self, ld):
        if ld is None or isinstance(ld, Medic):
            self.__link_doctor = ld

    def improve_status(self):
        if self.__status > 0:
            self.set_status(self.__status - 1)

    def worsen_status(self):
        if self.__status < 5:
            self.set_status(self.__status + 1)
