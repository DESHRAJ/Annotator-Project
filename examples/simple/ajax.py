import simplejson 

from dajaxice.decorators import dajaxice_register
#from dajax.core import Dajax 

@dajaxice_register(method='GET', name='simple.getitem')
def getitem(request, argu):
    arguu = str(argu)
    arguu = arguu[11:]
    with open('write.json','r') as f:
        while True:
    	    l = f.readline()
            line = l.rstrip()
            if(str(line).find(arguu)>0):
                final = line
                break
    f.close()
    return simplejson.dumps({'message': '%s' % final})

@dajaxice_register(method='GET')
@dajaxice_register(method='POST', name='other_post')
def hello(request):
    return simplejson.dumps({'message': 'hello'})


@dajaxice_register(method='GET')
@dajaxice_register(method='POST', name="more.complex.bye")
def bye(request):
    raise Exception("PUMMMM")
    return simplejson.dumps({'message': 'bye'})


@dajaxice_register
def lol(request):
    return simplejson.dumps({'message': 'lol'})


@dajaxice_register(method='GET')
def get_args(request, foo):
    f = open('write.json','a')
    f.write(foo+ '\n')
    f.close()
    return simplejson.dumps({'message': ' %s' % foo})
'''
    /*Dajaxice.simple.getitem(function(final){c=final},{'arg':a})*/

'''