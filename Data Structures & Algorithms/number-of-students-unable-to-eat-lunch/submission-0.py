class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        
        # have an accumulator that keeps track of the length of the queue (Students)
        # if we the accumulator >= length of the queue, this means there
        # are no sandwiches left for the students to take.

        acc = 0
        while acc < len(students):
            if students[0] == sandwiches[0]: # we found a match, pop from both
                print("Match found")
                students.pop(0)
                sandwiches.pop(0)
                acc = 0
            else:
                print(f"no match found {students[0]}, {sandwiches[0]}")
                # no match and then put the student in the back of the line
                student = students.pop(0)
                students.append(student)
                acc += 1

        if students:
            return len(students)

        return 0