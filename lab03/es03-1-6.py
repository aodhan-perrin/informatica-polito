def check(p: bool, q: bool, operator: str, isApplied: bool) -> bool:
    if isApplied:
        match operator:
            case "and":
                return (not p) or (not q)
            case "or":
                return (not p) and (not q)
    else:
        match operator:
            case "and":
                return not (p and q)
            case "or":
                return not (p or q)
                
                
def DeMorgan(p: bool, q: bool, operator: str, pre: str, post: str):
    print(
        f"{pre}: {check(p, q, operator, False)}\n"
        f"is equivlent to:\n"
        f"{post}: {check(p, q, operator, True)}\n"
    )


x = 1

DeMorgan(x > 0, x < 100, "and", f"¬({x} > 0 ∧ {x} < 100)", f"¬({x} > 0) ∨ ¬({x} < 100)")
DeMorgan(x > 0, x < 100, "or", f"¬({x} > 0 ∨ {x} < 100)", f"¬({x} > 0) ∧ ¬({x} < 100)")
DeMorgan(x > 0, x > 100, "or", f"¬({x} > 0 ∨ {x} > 100)", f"¬({x} > 0) ∧ ¬({x} > 100)")
DeMorgan(x > 0, x == -1, "and", f"¬({x} > 0 ∧ {x} == -1)", f"¬({x} > 0) ∨ ¬({x} == -1)")