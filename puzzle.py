from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


def xor(symbol_a, symbol_b):
    return And(
        Or(symbol_a, symbol_b),
        Not(And(symbol_a, symbol_b))
    )


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # "A" can be either knight or knave
    xor(AKnight, AKnave),
    # when "A" is a knight, the must be a knight and a knave same time.
    Implication(AKnight, And(AKnight, AKnave)),
    # when "A" is a knave, then he lies, he can't be a knight and a knave same time.
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # "A" can be either knight or knave
    xor(AKnight, AKnave),
    # "B" can be either knight or knave
    xor(BKnight, BKnave),
    Biconditional(
        # if "A" is a knave,
        AKnave,
        # then "A" lies (they are not both knaves).
        Not(And(AKnave, BKnave)),
    ),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    xor(AKnight, AKnave),
    xor(BKnight, BKnave),
    # if "A" is a knight, then "A" & "B" are both knights ("We are the same kind").
    Implication(AKnight, And(AKnight, BKnight)),
    # if "B" is a knight, then "A" & "B" are not same ("We are of different kinds)"
    Implication(BKnight, And(BKnight, AKnave)),
    # if "A" is a knave, "A" & "B" are different kinds
    Implication(AKnave, Not(And(AKnave, BKnave))),
    # if "B" is a knave, they are the same kind.
    Implication(BKnave, xor(And(AKnave, BKnave), And(AKnight, BKnight))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Rules
    xor(AKnight, AKnave),
    xor(BKnight, BKnave),
    xor(CKnight, CKnave),
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(xor(AKnight, AKnave))),
    # B says "C is a knave."
    # | If "B" is a knight
    Implication(BKnight, CKnave),
    # | If "B" is a knave
    Implication(BKnave, Not(CKnave)),
    # "C" says "A is a knight."
    # | If "C" is a knave
    Implication(CKnave, Not(AKnight)),
    # | If "C" is a knight
    Implication(CKnight, AKnight),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
