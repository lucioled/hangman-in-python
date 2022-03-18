from sqlite3 import DatabaseError


if __name__ == "__main__":
    DATA = [
        {
            'name': 'Facundo',
            'age': 72,
            'organization': 'Platzi',
            'position': 'Technical Coach',
            'language': 'python',
        },
        {
            'name': 'Luisana',
            'age': 33,
            'organization': 'Globant',
            'position': 'UX Designer',
            'language': 'javascript',
        },
        {
            'name': 'Héctor',
            'age': 19,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'ruby',
        },
        {
            'name': 'Gabriel',
            'age': 20,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'javascript',
        },
        {
            'name': 'Isabella',
            'age': 30,
            'organization': 'Platzi',
            'position': 'QA Manager',
            'language': 'java',
        },
        {
            'name': 'Karo',
            'age': 23,
            'organization': 'Everis',
            'position': 'Backend Developer',
            'language': 'python',
        },
        {
            'name': 'Ariel',
            'age': 32,
            'organization': 'Rappi',
            'position': 'Support',
            'language': '',
        },
        {
            'name': 'Juan',
            'age': 17,
            'organization': '',
            'position': 'Student',
            'language': 'go',
        },
        {
            'name': 'Pablo',
            'age': 32,
            'organization': 'Master',
            'position': 'Human Resources Manager',
            'language': 'python',
        },
        {
            'name': 'Lorena',
            'age': 56,
            'organization': 'Python Organization',
            'position': 'Language Maker',
            'language': 'python',
        },
    ]


platzi_workers = list(map(lambda worker: worker["name"], filter(
    lambda worker: worker["organization"] == "Platzi", DATA)))

old_workers = [worker["name"] + "-" + worker["organization"]
               for worker in DATA if worker["age"] >= 50]


print(platzi_workers)
print(old_workers)
