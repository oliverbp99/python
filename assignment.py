# 1. task

board_of_directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
Management = {'Tine', 'Trunte', 'Rane'}
Employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# - All except Tine is not an employee
# - Tina is the only one
# - Only Tine
# - False
# - True
# - Tine
# - Niels, Anna, Ole, Bent, Allan, Stine, Claus, James, Lars

# 2. task

tuples = [('a', 'Alpha'), ('b', 'Beta'), ('g', 'Gamma')]

print(tuples)

# 3. task

a = {'a', 'e', 'i', 'o', 'u', 'y'}

b = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Union
union =  a.union(b)

print(union)

# Symmetric difference

print(a ^ b)

# Difference

print(a.difference(b))

# Disjoint
disjoint =  a.isdisjoint(b)
print(disjoint)

# 4. task

monthDict = {'JAN': 1, 
            'FEB': 2, 
            'MAR': 3, 
            'APR': 4, 
            'MAY': 5, 
            'JUN': 6, 
            'JUL': 7, 
            'AUG': 8, 
            'SEP': 9, 
            'OCT': 10, 
            'NOV': 11, 
            'DEC': 12}
print(monthDict["JAN"])

def getMonth(date):
    newVar = date.split('-')
    newVar.reverse()

    xx = '20' + newVar[0], monthDict[newVar[1]], newVar[2]
    print(xx)


getMonth('8-DEC-95')


