class Optimization:
    
    def __init__(self,learningRate=0.1):
        self.lr=learningRate
        
        
    def step(self,layers):
        
        for layer in layers:
            
            w,b=layer.getParams()
            dw,db=layer.getGrads()
            
            #updating the layer parameters 
            w=w-lr*dw
            b=b-lr*db
            
            #storing the new parameters in layer
            layer.setParams(w,b)
            
