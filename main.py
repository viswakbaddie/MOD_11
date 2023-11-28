class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        pass


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


# Main Program
if __name__ == "__main__":
    donald_duck_magazine = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6_book = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck_magazine.print_information()
    print("------------------------")
    compartment_no_6_book.print_information()
