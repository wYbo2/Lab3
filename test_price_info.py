import price_info as core

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def test_total_cost():
    total = 46.75
    result = core.total_cost_shopping()
    assert(result == total)

def test_fruit_cost():
    cost = 6.0
    result = core.cost_of_fruits('apple', 5)
    assert(result == cost)
