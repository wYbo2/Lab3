import Lab2.lab2_bmi as bmi
print("Lab 3 test bmi Lab 2")

def test_bmi_normal_weight():
    result = bmi.calc_bmi(1.7,70)
    test_reult = 0
    assert(result==test_reult)
    

def test_bmi_over_weight():
    result = bmi.calc_bmi(1.7, 90)
    test_reult = 1
    assert(result==test_reult)

def test_bmi_under_weight():
    result = bmi.calc_bmi(1.7, 50)
    test_reult = -1
    assert(result==test_reult)
    


#test_bmi_normal_weight()
#test_bmi_over_weight()
#test_bmi_under_weight()