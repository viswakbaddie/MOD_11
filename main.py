class Publication():
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication's name is {self.name}")


class Book(Publication):
    def __init__(self, name, author, pageCount):
        super().__init__(name)
        self.author    = author
        self.pageCount = pageCount

    def print_information(self):
        super().print_information()
        print(f"Publication is a book:\n"
              f"Written by {self.author} with {self.pageCount} pages\n")


class Magazine(Publication):
    def __init__(self, name, chiefEditor):
        super().__init__(name)
        self.chiefEditor = chiefEditor

    def print_information(self):
        super().print_information()
        print(f"Publication is a magazine,\n"
              f"Whose chief editor is {self.chiefEditor}\n")


book     = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyyppä")

book.print_information()
magazine.print_information()