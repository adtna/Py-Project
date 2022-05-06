# importing the module
from chempy import chemistry

# creating the reaction
reaction = chemistry.Reaction({'H2': 2, 'O2': 1},
							{'H2O': 2})

# displaying the reaction
print(reaction)

# displaying the reaction order
print(reaction.order())
