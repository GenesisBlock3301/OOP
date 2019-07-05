class Bangladesh():

    def capital(self):
        print("Dhaka is the capital of india")

    def language(self):
        print("Bangla is the primary language in our country")

    def type(self):
        print("Bangladesh is developing country")


class USA():

    def capital(self):
        print("Washington is the capital of india")

    def language(self):
        print("English is the primary language in our country")

    def type(self):
        print("USA is developed country")

bd = Bangladesh()
bd.capital()
us = USA()
us.capital()


for i in (bd,us):
    bd.capital()
    bd.language()
    bd.type()