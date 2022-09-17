from pulp import *

path_to_cplex = "/Applications/CPLEX_Studio221/cplex/bin/x86-64_osx/cplex"
model = LpProblem("Example", LpMinimize)
solver = CPLEX_CMD(path=path_to_cplex)
_var = LpVariable('a')
_var2 = LpVariable('a2')
model += _var + _var2 == 1
result = model.solve(solver)
print(result)

solver_list = listSolvers(onlyAvailable=True)
print(solver_list)
# Lender information
lender_ids = ["L1", "L2", "L3"]

a = {"L1": 600, "L2": 800, "L3": 200}

b_1 = {"L1": 1.7, "L2": 2.1, "L3": 4.5}
b_2 = {"L1": 2.5, "L2": 2.9, "L3": 5.2}

b = {"L1": 2.0, "L2": 2.5, "L3": 4.8}

c_1 = {"L1": 4, "L2": 1, "L3": 1}
c_2 = {"L1": 10, "L2": 2, "L3": 4}

# Borrower Information
borrower_ids = ["B1"]

k_1 = {"B1": 210}
k_2 = {"B1": 250}
k = {"B1": 230}

t_1 = {"B1": 3}
t_2 = {"B1": 6}
t = {"B1": 4}


