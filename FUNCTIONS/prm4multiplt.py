class dance:
    def dancing (self):
        print("i can dance")
class fly:
    def flying(self):
        print("i can fly also")
class peacock(dance,fly):
    def sound(self):
        print("i had a good sound tooo")

p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
