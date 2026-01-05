def And(a, b):
    return a and b

def Or(a, b):
    return a or b

def Not(a):
    return not a

def Implies(a, b):
    return not a or b

def evaluate(expression, assignment):
    values = dict(assignment)
    p = values.get('p', False)
    q = values.get('q', False)
    r = values.get('r', False)
    return expression(p, q, r)

def kb(p, q, r):
    return And(Implies(p, q), Implies(q, r))

def query(p, q, r):
    return Implies(p, r)

def generate_truth_assignments():
    return [
        [('p', True), ('q', True), ('r', True)],
        [('p', True), ('q', True), ('r', False)],
        [('p', True), ('q', False), ('r', True)],
        [('p', True), ('q', False), ('r', False)],
        [('p', False), ('q', True), ('r', True)],
        [('p', False), ('q', True), ('r', False)],
        [('p', False), ('q', False), ('r', True)],
        [('p', False), ('q', False), ('r', False)]
    ]
    
def check_entailment(kb, query):
    truth_assignments = generate_truth_assignments()
    for assignment in truth_assignments:
        kb_result = evaluate(kb, assignment)
        query_result = evaluate(query, assignment)
        if kb_result and not query_result:
            return False
    return True

if check_entailment(kb, query):
    print("The knowledge base entails the query.")
else:
    print("The knowledge base does not entail the query.")
