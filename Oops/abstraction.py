from abc import ABC,abstractmethod
class LibraryItem(ABC):
    def __init__(self,title,item_id,):
        self.title=title
        self.item_id=item_id
     
    @abstractmethod
    def check_out(self):
        pass
    def return_item(self):
        pass
    def display_details(self):
        pass
class Book(LibraryItem):
    def __init__(self, title, item_id,author,genre):
        super().__init__(title, item_id)
        self.author=author
        self.genre=genre
    def check_out(self):
        return f"the book of title {self.title},item id {self.item_id}, author {self.author},and genre {self.genre} has been checked out"
    def return_item(self):
        return f"the book of title {self.title},item id {self.item_id}, author {self.author},and genre {self.genre} has been returned"
    def display_details(self):
        return f"the book of title {self.title} has author {self.author} and genre {self.genre}" 
class DVD(LibraryItem):
    def __init__(self, title, item_id,director,duration):
        super().__init__(title, item_id)
        self.director=director
        self.duration=duration
    def check_out(self):
        return f"the DVD of title {self.title},item id {self.item_id}, director {self.director},and duration {self.duration} minutes has been checked out"
    def return_item(self):
        return f"the DVD of title {self.title},item id {self.item_id}, director {self.director},and duration {self.duration} minutes has been returned"
    def display_details(self):
        return f"the DVD of title {self.title} has director {self.director} and duration {self.duration} minutes" 
b=Book('Tales',201,'Charles','Mystery')
d=DVD('Hangover201',101,'Gillespie',200)
print(b.check_out())
print(b.return_item())
print(b.display_details())
print(d.check_out())
print(d.return_item())
print(d.display_details())

    
        
    
