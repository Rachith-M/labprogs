def is_variable(term):
    return isinstance(term , str) and term.islower()

def substitute(theta, term):
    if term in theta:
        return theta[term]
    return term

def unify(term1, term2, theta):
    if term1 == term2:
        return theta
    if is_variable(term1):
        if term1 in theta:
            return unify(substitute(theta, term1), term2, theta)
        theta[term1] = term2
        return theta
    if is_variable(term2):
        return unify(term2, term1, theta)
    if isinstance(term1, tuple) and isinstance(term2, tuple) and len(term1) == len(term2):
        for t1, t2 in zip(term1, term2):
            theta = unify(t1, t2, theta)
            if theta is None:
                return None
        return theta
    return None

term1 = ('father', 'john', 'jane')
term2 = ('father', 'x', 'y')
theta = {}
result = unify(term1, term2, theta)

if result is not None:
    print(f"Unification succeeded: {result}")
else:
    print("Unification failed")
