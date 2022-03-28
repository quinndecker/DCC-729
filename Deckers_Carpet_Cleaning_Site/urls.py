from django.urls import path
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', views.homepage),	
    path('why-choose-us/', views.whychooseus),
    path('book-now/', views.booknow),
    

    #-Service Pages-#
    path('services/', views.servicedirectory),
    path('carpet/', views.carpetmain),
    path('upholstery/', views.upholsterymain),
    path('tile/', views.tilemain),
    path('stone/', views.stonemain),
    path('repairs/', views.repairmain),
    path('area-rugs/', views.arearugsmain),

    #-Layer 2 Carpet Pages-#
    path('carpet-cleaning/', views.carpetcleaning),
    path('carpet-cleaning/pet-stain-odor-treatment/', views.petstain),
    path('carpet-stretching/', views.carpetstretching),
    path('carpet-repair/', views.carpetrepair),
    path('commercial-carpet-cleaning/', views.commercialcarpetcleaning),
    path('advanced-spot-treatment/', views.advancedspot),
    path('carpet-protector', views.carpetprotector),

    #-Layer 2 Tile Pages-#
    path('tile-and-grout-cleaning/', views.tilegroutcleaning),
    path('grout-sealing/', views.groutsealing),
    path('grout-recoloring/', views.groutrecoloring),
    path('grout-repair/', views.groutrepair),
    path('commercial-tile-cleaning/', views.commercialtile),
    path('tile-floor-slip-reduction/', views.tileslipreduction),

    #-Layer 2 Upholstery Pages-#
    path('upholstery-cleaning-services/', views.upholsterycleaning),
    path('upholstery-repair/', views.upholsteryrepair),
    path('upholstery-protector/', views.upholsteryprotector),
    path('upholstery-pet-stain-odor/', views.uphpetstain),
    path('leather-cleaning-and-protector/', views.leathercleaning),
    path('auto-cleaning/', views.autocleaning),

    #-Layer 2 Stone Pages-#
    path('stone-floor-cleaning/', views.stonefloorcleaning),
    path('stone-honing-polishing-restoration/', views.stonehonepolish),
    path('stone-sealers/', views.stonesealers),
    path('granite-countertops/', views.granitecountertops),
    path('marble-travertine-limestone/', views.mtl),
    path('stone-backsplash-cleaning-and-sealing/', views.stonebacksplash),
    path('stone-repair/', views.stonerepair),
    path('commercial-stone-care/', views.commercialstone),
    path('stone-floor-slip-reduction/', views.stoneslipreduction),

    #-Layer 2 Area Rug Pages-#
    path('area-rug-cleaning/', views.arearugcleaning),
    path('area-rug-repair/', views.arearugrepair),

    ##Other Pages##
    path('stay-beautiful-club/', views.staybeautiful),
    path('service-area/', views.servicearea),
    path('commercial-services/', views.commericalservices),
    path('carpet-stretching-and-repair/', views.stretchrepair),
    path('water-damage-extraction/', views.waterdamage),
    path('stone-floor-and-countertop-care/', views.stonemain),
    path('commercial-service-directory/', views.commercialdirectory),
    path('pricing/', views.pricing),
    path('careers/', views.careers),
    path('meet-our-team/', views.meetourteam),





    ## THIS HAS TO BE LAST##
    #-Blog Functionality-#
    path('admin/', admin.site.urls),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    ##THIS HAS TO BE LAST##
]