class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Invalid name: must be a string")
        self.name = name
        self._contracts = []

    def contracts(self):
        """Returns a list of contracts associated with this author."""
        return self._contracts

    def books(self):
        """Returns a list of books associated with this author."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Creates a contract for an author and a book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Returns the sum of royalties of all contracts signed by the author."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Invalid title: must be a string")
        self.title = title
        self._contracts = []

    def contracts(self):
        """Returns a list of contracts associated with this book."""
        return self._contracts

    def authors(self):
        """Returns a list of authors who have contracts with this book."""
        return [contract.author for contract in self._contracts]


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        # Validation for Author, Book, Date, and Royalties
        if not isinstance(author, Author):
            raise Exception("Invalid author: must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Invalid book: must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Invalid date: must be a string")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties: must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add the contract to the book and author
        self.book._contracts.append(self)
        self.author._contracts.append(self)
        
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of contracts signed on a specific date, sorted by date."""
        filtered_contracts = [contract for contract in cls.all_contracts if contract.date == date]
        # Sort contracts by date (string comparison works here for 'DD/MM/YYYY' format)
        return sorted(filtered_contracts, key=lambda c: c.date)
