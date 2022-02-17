from simpleai.search import CspProblem, backtrack

# Define the function that imposes the constraint
# that neighbors should be different
def constraint_func(names, values):
    return values[0] != values[1]

if __name__=='__main__':
    # Specify the variables
    names = ('AlAxli', 'RMadrid', 'Barselona', 'Atlethic', 'Kolo',
            'AMadrid', 'Boka', 'Livpool', 'Boruss', 'Rades','CampNo','Enfild','SanSiro'
            ,'Yembli','Gambli')

    # Define the possible colors
    colors = dict((name, ['red', 'green', 'blue', 'gray']) for name in names)

    # Define the constraints
    constraints = [
        (('AlAxli', 'Atlethic'), constraint_func),
        (('AlAxli', 'RMadrid'), constraint_func),
        (('Atlethic', 'RMadrid'), constraint_func),
        (('Atlethic', 'Livpool'), constraint_func),
        (('Atlethic', 'AMadrid'), constraint_func),
        (('Livpool', 'AMadrid'), constraint_func),
        (('AMadrid', 'RMadrid'), constraint_func),
        (('AMadrid', 'Kolo'), constraint_func),
        (('AMadrid', 'Boruss'), constraint_func),
        (('AMadrid', 'Rades'), constraint_func),
        (('RMadrid', 'Kolo'), constraint_func),
        (('RMadrid', 'Barselona'), constraint_func),
        (('Kolo', 'Barselona'), constraint_func),
        (('Kolo', 'Boruss'), constraint_func),
        (('Kolo', 'Rades'), constraint_func),
        (('Barselona', 'CampNo'), constraint_func),
        (('Barselona', 'Boruss'), constraint_func),
        (('Boruss', 'Rades'), constraint_func),
        (('Boruss', 'Yembli'), constraint_func),
        (('Boruss', 'SanSiro'), constraint_func),
        (('Boruss', 'CampNo'), constraint_func),
        (('Rades', 'Boka'), constraint_func),
        (('Rades', 'Yembli'), constraint_func),
        (('CampNo', 'SanSiro'), constraint_func),
        (('SanSiro', 'Yembli'), constraint_func),
        (('Yembli', 'Boka'), constraint_func),
        (('Yembli', 'Enfild'), constraint_func),
        (('Boka', 'Enfild'), constraint_func),
        (('Boka', 'Gambli'), constraint_func),
    ]

    # Solve the problem
    problem = CspProblem(names, colors, constraints)

    # Print the solution
    output = backtrack(problem)
    print('\nColor mapping:\n')
    for k, v in output.items():
        print(k, '==>', v)
