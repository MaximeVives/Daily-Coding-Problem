courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
no_sort = {"CSC300": [], "CSC200": [], "CSC100": ["CSC050"]}


list_of_course = []

test = sorted(courses, key=lambda k: len(courses[k]), reverse=True)
# print(test)


for course in courses:
    list_of_course.append(course)
    for c in courses[course]:
        if c not in list_of_course:
            list_of_course.append(course)

