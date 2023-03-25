
import numpy
import warnings
from numpy import exp, array, random, asmatrix, matmul, add

warnings.filterwarnings('ignore')
class NeuralNetwork():
    def __init__(self,layers):
        fweights=open("api\Weights.txt","r+")
        fbaises=open("api\Baises.txt","r+")
        self.layers=layers
        self.maxexamples=50
        self.weightchanges=[]
        self.baischanges=[]
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
        
    def __createFileW(self,f):
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
            arrays.append(array)
            array=[]
        f.write(out)
        return arrays
    
    def __createFileB(self,f):
        out,arrays,array='',[],[]
        for i in range(len(self.layers)-1):
            layer=self.layers[i+1]
            for j in range(layer-1):
                array.append([1.0])
                out+='1.0;'
            out+='1.0$'
            array.append([1.0])
            arrays.append(array)
            array=[]
        f.write(out)
        return arrays
    
    def __UpdateFilesW(self,f,l):
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
    
    def __UpdateFilesB(self,f,l):
        arrays,array=[],[]
        for i in range(len(self.layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                f.write(f"{float(l[i][j]):.10f}".rstrip("0")+';')
            f.write(f"{float(l[i][j+1]):.10f}".rstrip("0")+'$')
    
    def __UpdateWeightsAndBaises(self,weightchange,baischange):
        open("api\Weights.txt","r+").truncate(0)
        open("api\Baises.txt","r+").truncate(0)
        self.__UpdateFilesW(open("api\Weights.txt","at"),weightchange)
        self.__UpdateFilesB(open("api\Baises.txt","at"),baischange)
        
    def __fileDecomposition(self, f):
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
                    out.append(array)
                    array=[[]]
                else:
                    word+=text[count]
        except:
            return []
        else:
            return out
        
    def __sigmoid(self, x):
        return 1.0 / (1.0 + exp(-x,dtype='float64'))
    
    def __sigmoid_derivative(self, x):
        return x / (1.0 - x)
    
    def __matrixmul(self,ins1,ins2):
        m1,m2=numpy.asmatrix(ins1, dtype='float64'),numpy.asmatrix(ins2, dtype='float64')
        return numpy.matrix.getA(numpy.matmul(m1,m2))
    
    def __matrixadd(self,ins1,ins2):
        m1,m2=numpy.asmatrix(ins1, dtype='float64'),numpy.asmatrix(ins2, dtype='float64')
        return numpy.matrix.getA(numpy.add(m1,m2))
    
    def __matrixsub(self,ins1,ins2):
        for j in range(len(ins2)):
            for i in range(len(ins2[j])):
                ins2[j][i]=-ins2[j][i]
        return self.__matrixadd(ins1,ins2)
    
    def __matrixmeld(self,ins1,ins2):
        out=[]
        for j in range(len(ins2)):
            out.append([])
            for i in range(len(ins2[j])):
                out[j].append(ins1[j][i]*ins2[j][i])
        return out
    
    def __matrixtranspose(self,ins):
        m=numpy.asmatrix(ins, dtype='float64')
        return numpy.matrix.getA(numpy.matrix.transpose(m))
    
    def __reduce(self,ins):
        out=self.__matrixadd(ins[0],ins[1])
        for i in range(2,len(ins)):
            out=self.__matrixadd(out,ins[i])
        return out
    
    def __matrixmulconst(self,ins1,ins2):
        out=[]
        for j in range(len(ins2)):
            out.append([])
            for i in range(len(ins2[j])):
                out[j].append(ins1*ins2[j][i])
        return out
    
    def __findAverage(self,ins):
        out=[]
        for a in range(len(ins[0])):
            templist=[]
            for element in ins:
                templist.append(element[a])
            out.append(self.__matrixmulconst((1/len(ins)),self.__reduce(templist)))
        return out
    
    def __testevaluate(self, ins):
        m1,out,sigmoid=self.__encode(ins),[],numpy.vectorize(self.__sigmoid)
        for i in range(len(self.weights)):
            m2 = self.__matrixmul(self.weights[i],m1)
            m3 = self.__matrixadd(m2,self.baises[i])
            m1 = sigmoid(m3)
            out.append(m1)
        return out
    
    def evaluate(self, ins):
        l=self.__testevaluate(ins)
        out=l[-1]
        return self.__decode(out)
    
    def __encode(self,ins):
        out,piecedict=[],{'MT':[[0],[0],[0],[0]],'WP':[[0],[0],[0],[1]],'BP':[[0],[0],[1],[0]],'WB':[[0],[0],[1],[1]],'BB':[[0],[1],[0],[0]],'WN':[[0],[1],[0],[1]],'BN':[[0],[1],[1],[0]],'WR':[[0],[1],[1],[1]],'BR':[[1],[0],[0],[0]],'WQ':[[1],[0],[0],[1]],'BQ':[[1],[0],[1],[0]],'WK':[[1],[1],[0],[1]],'BK':[[1],[1],[1],[0]]}
        for j in range(8):
            for i in range(8):
                out=piecedict[ins[j][i]]+out
        return out
    
    def __decode(self,ins):
        m=''
        for a in ins:
            m+=str(int(round(a[0])))
        if m[0]=='1':exponent=-(int(self.__bintoint(self.__twoscompliment(m[0:4]))))
        else:exponent=int(self.__bintoint(m[0:4]))
        mantissa=float(self.__bintoint(m[3:-1]))*0.03125
        out=mantissa*(2**exponent)
        if out>1.0:out=1.0
        elif out<0.001:out=0
        return out
    
    def __bintoint(self,ins):
        out,ins=0,ins[::-1]
        for i in range(len(ins)):
            x=1
            if ins[i]=='1':
                for a in range(i):
                    x*=2
                out+=(x)
        return out
    
    def __twoscompliment(self,ins):
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
    
    def __backprop(self,weights,baises,activations,expected):#  C′(W)=(O−y)⋅R′(Z)⋅H         where C'(w) is the rate of change of the ocst function with respect to the weights, O is the output of the function, y in the expected value, R'(Z) is the sum of the previos layer's activation times their respective weights put into the derivitive of the sigmoid function, H is the previos layer's activation. explanaition: https://ml-cheatsheet.readthedocs.io/en/latest/backpropagation.html 
        #  W=W-ΔW       ΔW=Error of layer infront * activation of previos Layer * learning rate
        weights,baises,activations,sigmoidDerivative=weights[::-1],baises[::-1],activations[::-1],numpy.vectorize(self.__sigmoid_derivative)
        observed,weight=activations[0],weights[0]
        
        error=self.__matrixsub(observed,expected)
        Z=[self.__matrixmul(weights[0],activations[1])]
        E=[self.__matrixmeld(sigmoidDerivative(Z[0]),error)]
        deltaW=[self.__matrixtranspose(self.__matrixmulconst(self.learning_rate,self.__matrixmul(activations[1], self.__matrixtranspose(E[0]))))]
        
        for i in range(1,len(weights)-1):
            Z.append(self.__matrixmul(weights[i],activations[i+1]))
            E.append(self.__matrixmeld(self.__matrixmul(self.__matrixtranspose(weights[i-1]),E[-1]),sigmoidDerivative(Z[i])))
            deltaW.append(self.__matrixtranspose(self.__matrixmulconst(self.learning_rate,self.__matrixmul(activations[i+1], self.__matrixtranspose(E[i])))))
        
        Z.append(self.__matrixmul(weights[-1],activations[-1]))
        E.append(self.__matrixmeld(self.__matrixmul(self.__matrixtranspose(weights[-2]),E[-1]),sigmoidDerivative(Z[-1])))
        deltaW.append(self.__matrixtranspose(self.__matrixmulconst(self.learning_rate,self.__matrixmul(activations[-1], self.__matrixtranspose(E[-1])))))
        #the change in bais is equal to the error, or E, for each of the layers
        return deltaW[::-1],E[::-1]  
    
    def train(self,example):
        activations=self.__testevaluate(example[0])
        change=self.__backprop(self.weights,self.baises,[self.__encode(example[0])]+activations,example[1])
        self.weightchanges.append(change[0])
        self.baischanges.append(change[1])
        if len(self.weightchanges)>=self.maxexamples:
            print('training in process.......')
            avrWeightChanges,avrBaisChanges,newweights,newbaises=self.__findAverage(self.weightchanges),self.__findAverage(self.baischanges),[],[]
            for i in range(len(avrWeightChanges)):
                newweights.append(self.__matrixsub(self.weights[i],avrWeightChanges[i]))
                newbaises.append(self.__matrixsub(self.baises[i],avrBaisChanges[i]))
            self.weights,self.baises=newweights,newbaises
            self.__UpdateWeightsAndBaises(self.weights,self.baises)
            self.weightchanges,self.baischanges=[],[]
            return


if __name__ =="__main__":
    import time
    NNUE=NeuralNetwork([4*64,64,10])
    T,avr=[],0
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