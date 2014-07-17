# Create your views here.
from django.shortcuts import *

from dajaxice.core import dajaxice_functions


#def index12(request):
#
#    return render(request, 'simple/index.html')

def index(request):

    return render(request, 'simple/Annotate.html')
