import numpy
import json

json_file = open('dataset.json', 'r')
json_decoded = json.load(json_file)

pixel = numpy.load('pixel_rep.npy')
vgg = numpy.load('vgg_rep.npy')

#cosine_similarity
def cosine_Similarity(v1,v2):
    m = numpy.dot(v1,v2)/(numpy.sqrt(numpy.dot(v1,v1)) * numpy.sqrt(numpy.dot(v2,v2)))
    return m

# nn algorithm
def nn(train,test):
    max = -1
    image = None
    for train_key in train.keys():
        temp = cosine_Similarity(train[train_key], test)
        if (temp > max):
            max = temp
            image = train_key
    return json_decoded['captions'][image]

#form train of pixel and train of vvg
train_vp = {}
train_vv = {}
for p in json_decoded[u'train']:
    index = json_decoded[u'images'].index(p)
    train_vp[p] = pixel[index]
    train_vv[p] = vgg[index]

#prediction list
predict_vp = []
predict_vv = []
for n in json_decoded[u'test']:
    index = json_decoded[u'images'].index(n)
    test_vp = pixel[index]
    predict_vp.append(nn(train_vp,test_vp))
    test_vv = vgg[index]
    predict_vv.append(nn(train_vv, test_vv))

# output vgg.txt
f = open('vgg.txt', 'w')
for name in predict_vv:
    f.write(name + '\n')
f.close()

# output pixel.txt
f = open('pixel.txt', 'w')
for name in predict_vp:
    f.write(name + '\n')
f.close()

# output the captions of test images
f = open('test.txt', 'w')
for name in json_decoded['test']:
    f.write(name + '   ' + json_decoded['captions'][name] + '\n')
f.close()