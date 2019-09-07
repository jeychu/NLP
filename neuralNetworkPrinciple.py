# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

content = pd.read_csv('/Users/CnuipMac/Documents/NLP/titanic.csv')
content = content.dropna()
age_with_fares = content[
    (content['Age'] > 22) & (content['Fare'] < 400) & (content['Fare'] > 130)
]
sub_fare = age_with_fares['Fare']
sub_age = age_with_fares['Age']

plt.scatter(sub_age, sub_fare)
plt.show()

def func(age, k, b): return k * age + b

def loss(y, yhat):
    """
    :param y: the real fares
    :param yhat: the estimated fares
    :return: how good is the estimated fares
    """
    return np.mean(np.abs(y - yhat))
    #return np.mean(np.sqrt(y - yhat))

min_error_rate = float('inf')

best_k, best_b = None, None

k_hat = random.random() * 20 - 10
b_hat = random.random() * 20 - 10

change_direction = [
        # (k, b)
        (+1, -1),
        (+1, +1),
        (-1, -1),
        (-1, +1)
        ]

best_direction = None

def step(): return random.random() * 1

def derivate_k(y, yhat, x):
    abs_values = [1 if (y_i - yhat_i) > 0 else -1 for y_i, yhat_i in zip(y, yhat)]
    return np.mean([a * -x_i for a, x_i in zip(abs_values, x)])

def derivate_b(y, yhat):
    abs_values = [1 if (y_i - yhat_i) > 0 else -1 for y_i, yhat_i in zip(y, yhat)]
    return np.mean([a * -1 for a in abs_values])
  
learing_rate = 1e-3
    
loop_time = 10000

while loop_time > 0:
    k_delta = -1 * learing_rate * derivate_k(sub_fare, func(sub_age, k_hat, b_hat), sub_age)
    b_delta = -1 * learing_rate * derivate_b(sub_fare, func(sub_age, k_hat, b_hat))
    
#    k_delta_direction, b_delta_direction = best_direction or \
#    random.choice(change_direction)
#    
#    k_delta = k_delta_direction * step()
#    b_delta = b_delta_direction * step()
    
    k_hat += k_delta
    b_hat += b_delta
    
    estimated_fares = func(sub_age, k_hat, b_hat)
    error_rate = loss(y=sub_fare, yhat=estimated_fares)
    
    print(error_rate)
    
#    if error_rate < min_error_rate:
#        min_error_rate = error_rate
#        best_k, best_b = k_hat, b_hat
#        
#        best_direction = (k_delta_direction, b_delta_direction)
#        
#        print(min_error_rate)
#        print('loop == {}'.format(loop_time))
#    else:
#        best_direction = random.choice(change_direction)
        
    loop_time -= 1
    
plt.scatter(sub_age, sub_fare)
plt.plot(sub_age, estimated_fares, c='r')
plt.show()