class Pizza():
    def __init__(self, ingrediant):
        self.ingrediant = ingrediant

    def __repr__(self):
        return f'Pizza({self.ingrediant!r})'


print(Pizza(['cheese', "tomatoes"]))