class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, add_name:str):
        self.add_name = add_name
        print("The new name of the student is ", add_name)
    
    def change_age(self, add_age:int):
        self.add_age = add_age
        print("The new age of the student is ", add_age)

    def add_track(self, add_tracks:str):
        self.add_tracks = add_tracks
        print("The new track of the student is ", add_tracks)

    def get_score(self, get_scores:float):
        self.get_scores = get_scores
        print("The score of the new student is ", get_scores)


   




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(23.04)


get_score =  34.05