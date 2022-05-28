class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name 
        self.age = age
        self.tracks = tracks
        self.score = score
        #print("my name is", name, "I am ", age, "these are my tracks", tracks, "and this is my score", score)
    def change_name(self, new_name):
        self.name = new_name
        print(self.name)
        return

    def change_age(self, new_age):
        self.age = new_age
        print(self.age)
        return

    def get_score(self):
        print(self.score)
        return

    def add_track(self, new_track):
        self.tracks.append(new_track) 
        print(self.tracks)
        return 


Bob = Student("Bob", 26, ["FE","BE"], 20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
