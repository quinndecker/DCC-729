from django.shortcuts import render, HttpResponse


def homepage(request): 
    return render(request, 'home2.html')
def whychooseus(request):
    return render(request, 'whychooseus.html')
def booknow(request):
    return render(request, 'booknow.html')
##-service pages-##
def servicedirectory(request):
    return render(request, 'servicedirectory.html')
def carpetmain(request):
    return render(request, 'nav-pages/carpet-main.html')
def upholsterymain(request):
    return render(request, 'nav-pages/upholstery-main.html')
def tilemain(request):
    return render(request, 'nav-pages/tile-main.html')
def stonemain(request):
    return render(request, 'nav-pages/stone-main.html')
def repairmain(request):
    return render(request, 'nav-pages/repair-main.html')
def arearugsmain(request):
    return render(request, 'nav-pages/area-rugs-main.html')

## Layer 2 - Carpet Pages ##
def carpetcleaning(request):
    return render(request, 'layer-2/carpet/carpet-cleaning.html')
def petstain(request):
    return render(request, 'layer-2/carpet/pet-stain-odor-treatment.html')
def advancedspot(request):
    return render(request, 'layer-2/carpet/advanced-spot-treatment.html')
def carpetstretching(request):
    return render(request, 'layer-2/carpet/carpet-stretching.html')
def carpetrepair(request):
    return render(request, 'layer-2/carpet/carpet-repair.html')
def commercialcarpetcleaning(request):
    return render(request, 'layer-2/carpet/commercial-carpet-cleaning.html')
def carpetprotector(request):
    return render(request, 'layer-2/carpet/carpet-protector.html')

## Layer 2 - Tile Pages ##
def tilegroutcleaning(request):
    return render(request, 'layer-2/tile/tile-and-grout-cleaning.html')
def groutsealing(request):
    return render(request, 'layer-2/tile/grout-sealing.html')
def groutrecoloring(request):
    return render(request, 'layer-2/tile/grout-recoloring.html')
def groutrepair(request):
    return render(request, 'layer-2/tile/grout-repair.html')
def commercialtile(request):
    return render(request, 'layer-2/tile/commercial-tile-cleaning.html')
def tileslipreduction(request):
    return render(request, 'layer-2/tile/tile-floor-slip-reduction.html')

## Layer 2- Upholstery Pages ##
def upholsterycleaning(request):
    return render(request, 'layer-2/upholstery/upholstery-cleaning-services.html')
def upholsteryrepair(request):
    return render(request, 'layer-2/upholstery/upholstery-repair.html')
def upholsteryprotector(request):
    return render(request, 'layer-2/upholstery/upholstery-protector.html')
def uphpetstain(request):
    return render(request, 'layer-2/upholstery/upholstery-pet-stain-odor.html')
def leathercleaning(request):
    return render(request, 'layer-2/upholstery/leather-cleaning-and-protector.html')
def autocleaning(request):
    return render(request, 'layer-2/upholstery/auto-cleaning.html')

## Layer 2 Stone Pages ##
def stonefloorcleaning(request):
    return render(request, 'layer-2/stone/stone-floor-cleaning.html')
def stonehonepolish(request):
    return render(request, 'layer-2/stone/stone-honing-polishing-restoration.html')
def stonesealers(request):
    return render(request, 'layer-2/stone/stone-sealers.html')
def granitecountertops(request):
    return render(request, 'layer-2/stone/granite-countertops.html')
def mtl(request):
    return render(request, 'layer-2/stone/mtl.html')
def stonebacksplash(request):
    return render(request, 'layer-2/stone/stone-backsplash-cleaning-and-sealing.html')
def stonerepair(request):
    return render(request, 'layer-2/stone/stone-repair.html')
def granitecountertops(request):
    return render(request, 'layer-2/stone/granite-countertops.html')
def commercialstone(request):
    return render(request, 'layer-2/stone/commercial-stone-care.html')
def stoneslipreduction(request):
    return render(request, 'layer-2/stone/stone-floor-slip-reduction.html')

#Layer 2 Area Rug Pages##
def arearugcleaning(request):
    return render(request, 'layer-2/rugs/area-rug-cleaning.html')
def arearugrepair(request):
    return render(request, 'layer-2/rugs/area-rug-repair.html')

##--##
def waterdamage(request):
    return render(request, 'layer-2/water-damage-extraction.html')
#def commercialdirectory(request):
    #return render(request,'commercial-services.html')

## Blog Stuff ##

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

## Other Pages ##

def staybeautiful(request):
    return render(request, 'stay-beautiful-club.html')
def servicearea(request):
    return render(request, 'service-area.html')
def commericalservices(request):
    return render(request, 'commercial-services.html')
def pricing(request):
    return render(request, 'pricing.html')
def careers(request):
    return render(request, 'careers.html')
def meetourteam(request):
    return render(request, 'meet-our-team.html')
def privacypolicy(request):
    return render(request, 'privacy-policy.html')

#City Pages#

def thewoodlandscitypage(request):
    return render(request, 'city-pages/the-woodlands-tx-carpet-cleaning.html')
def atascocitacitypage(request):
    return render(request, 'city-pages/atascocita-tx-carpet-cleaning.html')