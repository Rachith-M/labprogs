from sympy import symbols,And, Or, Not, Implies, to_cnf

def convert_to_cnf(statement):
    p,q = symbols('p q')
    parsed_statement = eval(statement)
    converted_statement = to_cnf(parsed_statement,True)
    return converted_statement

if __name__ == "__main__":
    statement = "(Implies(p,q) & Implies(q,p))"
    result = convert_to_cnf(statement)
    print(f"Statement {statement} converted to cnf as: {result}")
