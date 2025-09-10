from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def start(self):

        pass

    @abstractmethod
    def execute(self):

        pass

    @abstractmethod
    def debug(self):

        pass


class Vscode(Editor):

    def start(self):
      
      print("vscode start using code .")


    def execute(self):
       
       print("Vscode executed the program")


    def debug(self):

        print("vscode debugged the program")


vscode_instance = Vscode()

vscode_instance.start()

vscode_instance.execute()

vscode_instance.debug()




