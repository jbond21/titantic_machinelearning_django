def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('/Users/jordanbond/Desktop/titantic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction == 0:
        prediction = 'dead'
    elif prediction == 1:
        prediction = 'survived'   
    else:
        prediction= 'error'     
    return prediction