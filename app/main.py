class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.tuple = (1, 2, 3, 4, 5)
        self.list = [1, 2, 3, 4]
        self.dict = {
            "coucou": "plop",
        }
        self.is_ok = True

    def hello(self):
        print(f"Je m'appelle {self.firstname} {self.lastname.upper()}")


user = User("Bernard", "Dupont")
