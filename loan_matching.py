from docplex.mp.model import Model


'''
Problem formulation
    Borrower Information
        k_1 is a vector where each number represents the min.
        amount a person would like to borrow. 
        k_2 is a vector where each number represents the max.
        amount a person would like to borrow.

        t_1 is a vector where each number represents the min.
        amount of time (in weeks) a person would like to borrow
        for.
        t_2 is a vector where each number represents the max.
        amount of time (in weeks) a person would like to borrow
        for.

    Lender Information
        a is a vector where each number represents the amount 
        a lender is willing to lend.
        b_1 is a vector where each number represents the min.
        interest rate a lender is willing to lend at.
        b_2 is a vector where each number represents the max.
        interest rate a lender is willing to lend at.
        b is a vector where each number represents the interest
        rate a lender has picked to lend at.
        c_1 is a vector where each number represents the min.
        amount of time (in weeks) a lender is willing to lend
        for.
        c_2 is a vector where each number represents the max.
        amount of time (in weeks) a lender is willing to lend
        for.
'''

k_1 = [210]
k_2 = [250]
t_1 = [3]
t_2 = [10]

a = [600, 800, 200, 300, 125, 540]
b_1 = [1.7, 2.1, 4.5]
b_2 = [2.5, 2.9, 5.2]
b = [0.02, 0.025, 0.048, 0.022, 0.031, 0.047]
c_1 = [1, 2, 2, 1, 1, 3]
c_2 = [10, 8, 12, 17, 6, 11]

vars_x = []
vars_y = []
indicators = []

model = Model(name='loan_matching')
model.parameters.optimalitytarget.set(3)

for i in range(len(a)):
    vars_x.append(model.continuous_var(name='x' + str(i)))
    vars_y.append(model.integer_var(name='y' + str(i)))
    indicators.append(model.binary_var(name='ind' + str(i)))
    

for i, min_borrow_amount in enumerate(k_1):
    model.add_constraint(model.sum(vars_x[j] * a[j] for j in range(len(vars_x))) >= min_borrow_amount, 'c3_' + str(i))

for i, max_borrow_amount in enumerate(k_2):
    model.add_constraint(model.sum(vars_x[j] * a[j] for j in range(len(vars_x))) <= max_borrow_amount, 'c4_' + str(i))

model.add_constraint(model.sum(vars_x[i] for i in range(len(vars_x))) == 1, )

for i, min_weeks in enumerate(c_1):
    model.add_indicator(indicators[i], vars_x[i] >= 0.00001, active_value=1)
    
    model.add_if_then(indicators[i] == 1, vars_y[i] >= min_weeks)
    model.add_if_then(indicators[i] == 1, vars_y[i] <= c_2[i])
    model.add_if_then(indicators[i] == 1, vars_y[i] <= t_1[0])
    model.add_if_then(indicators[i] == 1, vars_y[i] >= t_2[0])


avg = model.sum(vars_x[i] for i in range(len(vars_x))) / len(vars_x)
sd = (model.sum_squares((vars_x[i] - avg) for i in range(len(vars_x))) / len(vars_x)) 

model.minimize(model.sum(a[i] * b[i] * vars_x[i] for i in range(len(vars_x))) - sd)

s = model.solve()
print(s)
model.print_information()

