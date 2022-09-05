class Personel:
    def __init__(self):
        self.__id=0
        self.__name=""
        self.__gender=""
    def setPersonel(self):
        self.__id=int(input("Masukan Id: "))
        self.__name = input("Masukan Nama: ")
        self.__gender = input("Masukan Jenis Kelamin: ")
    def showPersonel(self):
        print("Id: ",self.__id)
        print("Nama: ",self.__name)
        print("Jenis Kelamin: ",self.__gender)

class Educational:
    def __init__(self):
        self.__stream=""
        self.__year=""
    def setEducational(self):
        self.__stream=input("Masukan Jurusan: ")
        self.__year = input("Masukan Tahun : ")
    def showEducational(self):
        print("Jurusan: ",self.__stream)
        print("Tahun: ",self.__year)

class Student(Personel,Educational):
    def __init__(self):
        self.__address = ""
        self.__contact = ""
    def setStudent(self):
        self.setPersonel()
        self.__address = input("Masukan Alamat: ")
        self.__contact = input("Masukan kontak: ")
        self.setEducational()

    def showStudent(self):
        self.showPersonel()
        print("Alamat: ",self.__address)
        print("Kontak: ",self.__contact)
        self.showEducational()

def main():
    s=Student()
    s.setStudent()
    s.showStudent()
if __name__=="__main__":main()