# Create a class, School, in the school.py file in your local directory that can be initialized with a name. The School class would be referred to as a "model" in the domain model context.

class School:

    #init is like your blueprint; this is where you decide what arguments every School object has and what data type they are
    def __init__(self, name, roster={}):
        self._name = name
        self._roster = roster

# A school should have a roster, which should be an empty dictionary upon initialization but will be built-out to contain keys of grade levels. The value of each key will be a list of student names (i.e. {"9": ["John Smith", "Jane Donahue"]}).
# You should be able to add a student to the school by calling the add_student method and giving it an argument of the student's name and their grade.
    def add_student(self, student_name, grade):
        if grade not in self._roster:
            self._roster[grade] = []
        self._roster[grade].append(student_name)

        return self._roster

# Next, define a method called grade, which should take in an argument of a grade and return a list of all the students in that grade:
    def grade(self,grade):
        return self._roster[grade]

# Define a method called sort_roster that returns the school's roster where the strings in the student arrays are sorted alphabetically. For instance: {9: ["Kelly Slater"], 10: ["Ryan Sheckler", "Tony Hawk"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}}
    def sort_roster(self):
        sorted_roster = {}
        for k,v in self._roster.items():
            sorted_roster[k] = sorted(v)
        return sorted_roster
        
