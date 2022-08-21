class Student:

    def __init__(self, firstname, lastname, id, programofstudy):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.programofstudy = programofstudy



Nick = Student("Nick", "O'Quinn", 20109408, "Software Development")
Cody = Student("Cody", "O'Quinn", 20109999, "English")

print(f"{Nick.firstname[0]}. {Nick.lastname}")
print(Cody.lastname)
print(Nick.id)
print(Cody.programofstudy)
