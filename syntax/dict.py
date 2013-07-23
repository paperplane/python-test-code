# use dict implement case-switch statements

def fun(x):
    # 3 for default value
    return {'foo':1,'bar':2}.get(x,3)
