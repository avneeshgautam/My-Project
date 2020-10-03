
        features=[fever,bodypain,age,runnynose,diffbreath]
        inf_prob = classifier.predict_proba([features])[0][1]
        print(inf_prob)