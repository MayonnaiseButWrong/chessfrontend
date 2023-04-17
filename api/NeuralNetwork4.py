
import numpy
import warnings
from numpy import exp, array, random, asmatrix, matmul, add
import tensorflow as tf

warnings.filterwarnings('ignore')   #filters all the warnings

@tf.function
def sigmoid(x): #defines the sigmoid function as a tesorflow function. the sigmoid function is used to get the activation of a neuron between 0 and 1. by making it a tensorflow function, it can be applied to a whole matrix at once and it can be parallelised to decrease the evaluation times
    return 1.0 / (1.0 + tf.math.exp(-x))

@tf.function
def sigmoid_derivative(x):# defines the derivative of the sigmoid as a tensorflow function, allowing it to be parallelised. This function gives the gradinet of the sigmoid function at any value of x. This function is used in the training of the NNUE
    return x / (1.0 - x)

class NeuralNetwork():  #instatiates the neural network as a class so that once the object is created it can be reused for every instace the NNUE is called. It also allows for the internal processes of the NNUE to be encapsulated within the object, hiding the complexity as a form of abstraction.
    def __init__(self,layers):
        fweights=open("api\Weights.txt","r+")
        fbaises=open("api\Baises.txt","r+")
        self.layers=layers
        self.maxexamples=50
        self.weightchanges=[]
        self.baischanges=[]
        self.examples=[]
        self.learning_rate = 1
        if len(str(fweights.read()))<1 or len(str(fbaises.read()))<1:
            fweights.truncate(0)
            fbaises.truncate(0)
            self.weights=self.__createFileW(open("api\Weights.txt","wt"))
            self.baises=self.__createFileB(open("api\Baises.txt","wt"))
        else:
            self.weights=self.__fileDecomposition(open("api\Weights.txt","rt"))
            self.baises=self.__fileDecomposition(open("api\Baises.txt","rt"))
            check=[len(self.weights[0][0])]
            for bais in self.baises:
                check.append(len(bais))
            if check!=self.layers:
                fweights.truncate(0)        #if there is a mismatch between the dimensions of the weights and baises found in the file and the input dimensions it means that there is an error and all of the weights have ot be generated from scratch
                fbaises.truncate(0)
                self.weights=self.__createFileW(open("api\Weights.txt","wt"))
                self.baises=self.__createFileB(open("api\Baises.txt","wt"))
        
    def __createFileW(self,f):  #weights stored in a text file so that training progress of the NNUE isnt lost
        out,arrays,array='',[],[]
        for i in range(len(self.layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                array.append([])
                for k in range(layer1-1):
                    out+='1.0,'
                    array[-1].append(1.0)
                out+='1.0;'
                array[-1].append(1.0)
            array.append([])
            for k in range(layer1-1):
                    out+='1.0,'
                    array[-1].append(1.0)
            out+='1.0$'
            array[-1].append(1.0)
            arrays.append(tf.constant(array, dtype='float64'))
            array=[]
        f.write(out)
        return arrays
    
    def __createFileB(self,f):#biases stored in a text file so that training progress of the NNUE isnt lost
        out,arrays,array='',[],[]
        for i in range(len(self.layers)-1):
            layer=self.layers[i+1]
            for j in range(layer-1):
                array.append([1.0])
                out+='1.0;'
            out+='1.0$'
            array.append([1.0])
            arrays.append(tf.constant(array, dtype='float64'))
            array=[]
        f.write(out)
        return arrays
    
    def __UpdateFilesW(self,f,l):#updating the weight files
        arrays,array=[],[]
        for i in range(len(self.layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                for k in range(layer1-1):
                    f.write(f"{float(l[i][j][k]):.10f}".rstrip("0")+',')
                f.write(f"{float(l[i][j][k+1]):.10f}".rstrip("0")+';')
            for m in range(layer1-1):
                    f.write(f"{float(l[i][j][m]):.10f}".rstrip("0")+',')
            f.write(f"{float(l[i][j][m+1]):.10f}".rstrip("0")+'$')
    
    def __UpdateFilesB(self,f,l):#updating the bais files
        arrays,array=[],[]
        for i in range(len(self.layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                f.write(f"{float(l[i][j]):.10f}".rstrip("0")+';')
            f.write(f"{float(l[i][j+1]):.10f}".rstrip("0")+'$')
    
    def __UpdateWeightsAndBaises(self,weightchange,baischange):#clearing both files anf calling the function for them to eb updated
        open("api\Weights.txt","r+").truncate(0)
        open("api\Baises.txt","r+").truncate(0)
        self.__UpdateFilesW(open("api\Weights.txt","at"),weightchange)
        self.__UpdateFilesB(open("api\Baises.txt","at"),baischange)
        
    def __fileDecomposition(self, f):   #gets the data from the file for either weights or baises depending on what is called
        text=str(f.read())
        word,array,out=text[0],[[]],[]
        try:
            for count in range(1,len(text)):
                if text[count]==',':
                    array[-1].append(float(word))
                    word=''
                elif text[count]==';':
                    array[-1].append(float(word))
                    word=''
                    array.append([])
                elif text[count]=='$':
                    array[-1].append(float(word))
                    word=''
                    out.append(tf.constant(array, dtype='float64'))
                    array=[[]]
                else:
                    word+=text[count]
        except:
            return []
        else:
            return out
    
    def __reduce(self,ins):#reduced the output without using recursion, as the is function is run so many times that it is already very close to the recursion limit, so if it used recursion it'd be go over the limit
        out=tf.math.add(ins[0],ins[1])
        for i in range(2,len(ins)):
            out=tf.math.add(out,ins[i])
        return out
    
    def __findAverage(self,ins):    #finds the average weight or bais
        out=[]
        for a in range(len(ins[0])):
            templist=[]
            for element in ins:
                templist.append(element[a])
            out.append(tf.multiply(1/len(ins),self.__reduce(templist)))
        return out
    
    def __testevaluate(self, ins):  #finds the activation of each layer in the nnue for a given input
        m1,out=self.__encode(ins),[]
        for i in range(len(self.weights)):
            m2 = tf.linalg.matmul(self.weights[i],m1)
            m3 = tf.math.add(m2,self.baises[i])
            m1 = sigmoid(m3)
            out.append(m1)
        return out
    
    def evaluate(self, ins):    #takes the last value from the test evaluate function and outputs it actr decoding it
        l=self.__testevaluate(ins)
        out=l[-1]
        return self.__decode(out)
    
    def __encode(self,ins):
        out,piecedict=[],{'MT':[[0],[0],[0],[0]],'WP':[[0],[0],[0],[1]],'BP':[[0],[0],[1],[0]],'WB':[[0],[0],[1],[1]],'BB':[[0],[1],[0],[0]],'WN':[[0],[1],[0],[1]],'BN':[[0],[1],[1],[0]],'WR':[[0],[1],[1],[1]],'BR':[[1],[0],[0],[0]],'WQ':[[1],[0],[0],[1]],'BQ':[[1],[0],[1],[0]],'WK':[[1],[1],[0],[1]],'BK':[[1],[1],[1],[0]]}
        for j in range(8):
            for i in range(8):
                out=piecedict[ins[j][i]]+out
        return tf.constant(out, dtype='float64')    #encodes a board layout into a binary  number so that it can be put into the neural netwok. this is often called a flattening layer but i personally don't like that terminology as this techincally isnt a part of the layer of the nnue
    
    def __decode(self,ins):
        m,ins='',ins.numpy()
        for a in ins:
            m+=str(int(round(a[0])))
        if m[0]=='1':exponent=-(int(self.__bintoint(self.__twoscompliment(m[0:4]))))
        else:exponent=int(self.__bintoint(m[0:4]))
        mantissa=float(self.__bintoint(m[3:-1]))*0.03125
        out=mantissa*(2**exponent)
        if out>1.0:out=1.0
        elif out<0.001:out=0
        return out  #returns a binary floating point number from the output of the nnue
    
    def __bintoint(self,ins):   #gets an intager from the nnue
        out,ins=0,ins[::-1]
        for i in range(len(ins)):
            x=1
            if ins[i]=='1':
                for a in range(i):
                    x*=2
                out+=(x)
        return out
    
    def __twoscompliment(self,ins): #uses twos compliment to find the intager value of a binary number
        flag,out=False,''
        for n in range(len(ins)):
            if n>len(ins):n=0
            if ins[-n]=='1' and flag==False:
                out='1'+out
                flag=True
            elif ins[-n]=='1':
                out='0'+out
            else:
                out='1'+out
        return out
    
    def __backprop(self,weights,baises,activations,expected): # used to train the nnue. every time theis function is run, one step of the training has been completed.
        #  C′(W)=(O−y)⋅R′(Z)⋅H         where C'(w) is the rate of change of the ocst function with respect to the weights, O is the output of the function, y in the expected value, R'(Z) is the sum of the previos layer's activation times their respective weights put into the derivitive of the sigmoid function, H is the previos layer's activation. explanaition: https://ml-cheatsheet.readthedocs.io/en/latest/backpropagation.html 
        #  W=W-ΔW       ΔW=Error of layer infront * activation of previos Layer * learning rate
        weights,baises,activations=weights[::-1],baises[::-1],activations[::-1]
        observed,weight=activations[0],weights[0]
        
        error=tf.math.add(observed,tf.multiply(-1,expected))
        Z=[tf.linalg.matmul(weights[0],activations[1])]
        E=[tf.multiply(sigmoid_derivative(Z[0]),error)] #fincing the change in weights and baises for the first layer
        deltaW=[tf.transpose(tf.multiply(self.learning_rate,tf.linalg.matmul(activations[1], tf.transpose(E[0]))))]
        
        for i in range(1,len(weights)-1):# using the previos layer to find the changes in weights and baises for the next layers
            Z.append(tf.linalg.matmul(weights[i],activations[i+1]))
            E.append(tf.multiply(tf.linalg.matmul(tf.transpose(weights[i-1]),E[-1]),sigmoid_derivative(Z[i])))
            deltaW.append(tf.transpose(tf.multiply(self.learning_rate,tf.linalg.matmul(activations[i+1], tf.transpose(E[i])))))
        
        Z.append(tf.linalg.matmul(weights[-1],activations[-1])) # finds the change in weights and baises for the last layer
        E.append(tf.multiply(tf.linalg.matmul(tf.transpose(weights[-2]),E[-1]),sigmoid_derivative(Z[-1])))
        deltaW.append(tf.transpose(tf.multiply(self.learning_rate,tf.linalg.matmul(activations[-1], tf.transpose(E[-1])))))
        #the change in bais is equal to the error, or E, for each of the layers
        return deltaW[::-1],E[::-1]  
    
    def train(self,ins):    #trainng the nnue
        self.examples.append([ins[0],tf.constant(ins[1], dtype='float64')])
        if len(self.examples)>=self.maxexamples:
            for example in self.examples:
                activations=self.__testevaluate(example[0])
                change=self.__backprop(self.weights,self.baises,[self.__encode(example[0])]+activations,example[1])
                self.weightchanges.append(change[0])
                self.baischanges.append(change[1])
            avrWeightChanges,avrBaisChanges,newweights,newbaises=self.__findAverage(self.weightchanges),self.__findAverage(self.baischanges),[],[]
            for i in range(len(avrWeightChanges)):
                newweights.append(tf.math.add(tf.multiply(-1,self.weights[i]),avrWeightChanges[i]))
                newbaises.append(td.math.add(tf.multiply(-1,self.baises[i]),avrBaisChanges[i]))
            self.weights,self.baises=newweights,newbaises
            self.__UpdateWeightsAndBaises(self.weights.numpy(),self.baises.numpy())
            self.weightchanges,self.baischanges=[],[]
        return


if __name__ =="__main__":   #used for testing
    import time
    T,avr=[],0
    NNUE=NeuralNetwork([4*64,64,10])
    for i in range(1000):
        start_time = time.time()
        NNUE.evaluate([['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']])
        T.append(time.time() - start_time)
    for a in range(len(T)):
        avr+=T[a]
    avr/=len(T)
    #for i in range(50):
    #    NNUE.train([[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']],[[0], [0], [0], [0], [0], [1], [1], [0], [0], [0]]])
    print('done')
    print("--- %s seconds ---" % (avr))
    # avr evaluation time improved to 0.0012592103481292726 seconds