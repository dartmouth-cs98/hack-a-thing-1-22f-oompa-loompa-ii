from docplex.mp.model import Model
import statistics

vars = []
model = Model(name='loan_matching')

for i in range(3):
    vars.append(model.continous_var(name='x' + str(i)))

y = model.integer_var(name='y')

for var, i in enumerate(vars):
    model.add_constraint(-var <= 0, 'c1_' + str(i))
    model.add_constraint(var <= 1, 'c2_' + str(i))

model.add_constraint(-sum(vars) <= 200, 'c3')
