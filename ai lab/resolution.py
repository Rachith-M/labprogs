def add_clause(knowledge_base, clause):
    knowledge_base.append(clause)

def complement(literal):
    """Return the complementary literal"""
    if literal.startswith("~"):
        return literal[1:]
    return "~" + literal

def resolve(clause1, clause2):
    for literal in clause1:
        comp = complement(literal)
        if comp in clause2:
            # Remove the complementary pair and merge remaining literals
            new_clause = []
            for x in clause1 + clause2:
                if x != literal and x != comp and x not in new_clause:
                    new_clause.append(x)
            return new_clause
    return None

def resolution(knowledge_base, query):
    # Negate the query
    negated_query = [complement(lit) for lit in query]
    print("Negated query added to KB:", negated_query)
    knowledge_base.append(negated_query)
    while True:
        new_clauses = []
        for i in range(len(knowledge_base)):
            for j in range(i + 1, len(knowledge_base)):
                resolvent = resolve(knowledge_base[i], knowledge_base[j])
                if resolvent == []:
                    print("Resolved", knowledge_base[i], "and",
                          knowledge_base[j], "→ []")
                    print("Contradiction found. The query is entailed.")
                    return True
                if resolvent and resolvent not in knowledge_base \
                   and resolvent not in new_clauses:
                    print("Resolved", knowledge_base[i], "and",
                          knowledge_base[j], "→", resolvent)
                    new_clauses.append(resolvent)
        if not new_clauses:
            print("No new clauses can be generated.")
            return False
        knowledge_base.extend(new_clauses)

# ----------- EXAMPLE USAGE (LOGICALLY CORRECT) ------------

kb = []
add_clause(kb, ["~P", "Q"])   # P → Q
add_clause(kb, ["P"])
query = ["Q"]
if resolution(kb, query):
    print("\nThe query is proved.")
else:
    print("\nThe query cannot be proved.")