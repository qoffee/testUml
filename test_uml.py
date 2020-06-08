class A:
    def __init__(self):
        self.b = B()

class BaseEstimator:
    def __init__(self):
        pass
    
    def fit(self):
        pass
    
    def predict(self):
        pass


class KNN(BaseEstimator):
    def __init__(self, **params):
        super().__init__(**params)
        
    def fit():
        pass
    
    def predict():
        pass
    
class LR(BaseEstimator):
    def __init__(self, **params):
        super().__init__(**params)
        
    def fit():
        pass
    
    def predict():
        pass

class RF(BaseEstimator):
    def __init__(self, **params):
        super().__init__(**params)
        
    def fit():
        pass
    
    def predict():
        pass

class XGB(BaseEstimator):
    def __init__(self, **params):
        super().__init__(**params)
        
    def fit():
        pass
    
    def predict():
        pass

    
class NN(BaseEstimator):
    def __init__(self, **params):
        super().__init__(**params)
        
    def fit():
        pass
    
    def predict():
        pass


MYVAR = 100
a = A()
b = B()

def calculate():
    return MYVAR
