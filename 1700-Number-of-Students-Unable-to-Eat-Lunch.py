class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        c = 0
        while c != len(students) and len(students) > 0:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                while c != len(students) and students[0] != sandwiches[0]:
                    students.append(students.pop(0))
                    c+=1
                if c == len(students):
                    break
                students.pop(0)
                sandwiches.pop(0)
                c=0
        return len(students)