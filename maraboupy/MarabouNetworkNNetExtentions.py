

from MarabouNetworkNNetExtended import *
from  MarabouNetworkNNet import *

def splitList(list,l):
    return list[:l], list[l:]

'''
Takes one MarabouNetworkNNEt object and layer, and returns two MarabouNetworkNNet objects, generated by cutting the original network
after the given layer. Note that the input layer is considered layer 0.
'''

def splitNNet(marabou_nnet: MarabouNetworkNNet, layer: int):
        if (layer < 1) or (layer > marabou_nnet.numLayers):
                print("nothing to do")
                return(False)
        weights1, weights2 = splitList(marabou_nnet.weights, layer)
        biases1, biases2 = splitList(marabou_nnet.biases, layer)

        layerSizes1, layerSizes2 = splitList(marabou_nnet.layerSizes,layer) #!TO ADD TO THE NEW NETWORKS!

        print("layesizes = ",marabou_nnet.layerSizes)
        print("layesizes1 = ",layerSizes1)
        print("layesizes2 = ",layerSizes2)

        new_input_size = marabou_nnet.layerSizes[layer + 1]

        mins1 = marabou_nnet.inputMinimums

        print(mins1)

        maxs1 = marabou_nnet.inputMaximums

        means1 = marabou_nnet.inputMeans
        ranges1 = marabou_nnet.inputRanges

        '''
        No normalization for the outputs of the first network
        '''
        means1[-1] = 0
        ranges1[-1] = 1

        '''
        The mins and maxs of the second input layer are taken to be the lower and the upper bounds of that layer,
        respectively
        '''

        # to implement!!!!
        
        #mins2,maxs2 = marabou_nnet.returnBounds(layer)

        #maxs2 = [0]*new_input_size  # Not sure!
        #mins2 = [0]*new_input_size  # Not sure!

        '''
        No normalization for the new input layer
        '''
        means2 = [0] * (new_input_size+1)
        ranges2 = [1] * (new_input_size+1)

        '''
        The mean and the range for the output for the second network are the mean and the range of 
        the original output
        '''
        means2[-1] = marabou_nnet.inputMeans[-1]
        ranges2[-1] = marabou_nnet.inputRanges[-1]

        # NOTE that these choices may affect the evaluations! One should be careful with applying normalization.

        marabou_nnet1 = MarabouNetworkNNetExtended()
        marabou_nnet2 = MarabouNetworkNNetExtended()

        marabou_nnet1.resetNetworkFromParameters(mins1, maxs1, means1, ranges1, weights1, biases1,numLayers=-1,layerSizes=layerSizes1)
        marabou_nnet2.resetNetworkFromParameters(mins2, maxs2, means2, ranges2, weights2, biases2,numLayers=-1,layerSizes=layerSizes2)


#        nnet1 = NNet(weights1, biases1, mins1, maxs1, means1, ranges1)
#        nnet2 = NNet(weights2, biases2, mins2, maxs2, means2, ranges2)

        return marabou_nnet1,marabou_nnet2




nnet = MarabouNetworkNNetExtended("../resources/nnet/acasxu/ACASXU_experimental_v2a_1_9.nnet")

print (type(MarabouNetworkNNet))




property_filename = "../resources/properties/acas_property_4.txt"
property_filename1 = "../resources/properties/acas_property_1.txt"
network_filename = "../maraboupy/regress_acas_nnet/ACASXU_run2a_1_7_batch_2000.nnet"

layer = 2

nnet_object = MarabouNetworkNNetExtended(filename=network_filename,property_filename=property_filename)

nnet_object1, nnet_object2 = splitNNet(marabou_nnet=nnet_object,layer=layer)


