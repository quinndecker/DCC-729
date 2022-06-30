from math import perm
from django.shortcuts import redirect, reverse

#redirects# 
def redirect_to_home(request):
    return redirect(reverse('deckersite:homepage'), permanent=True)
def redirect_to_about(request):
    return redirect(reverse('deckersite:whychooseus'), permanent=True)
def redirect_3(request):
    return redirect('/what-do-i-do-once-my-carpets-are-cleaned/', permanent=True)
def redirect_to_carpet_cleaning(request):
    return redirect(reverse('deckersite:carpetcleaning'), permanent=True)
def redirect_to_tile(request):
    return redirect(reverse('deckersite:tilemain'), permanent=True)
def redirect_to_pets(request):
    return redirect(reverse('deckersite:petstain'), permanent=True)
def redirect_to_booking(request):
    return redirect(reverse('deckersite:booknow'))
def redirect_to_areas(request):
    return redirect(reverse('deckersite:servicearea'), permanent=True)
    