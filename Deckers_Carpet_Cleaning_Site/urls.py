from django.urls import path
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', views.homepage, name='homepage'),	
    path('why-choose-us/', views.whychooseus, name='whychooseus'),
    path('book-now/', views.booknow, name='booknow'),
    

    #-Service Pages-#
    path('services/', views.servicedirectory, name='servicedirectory'),
    path('carpet/', views.carpetmain, name='carpetmain'),
    path('upholstery/', views.upholsterymain, name='upholsterymain'),
    path('tile/', views.tilemain, name='tilemain'),
    path('stone/', views.stonemain, name='stonemain'),
    path('repairs/', views.repairmain, name='repairmain'),
    path('area-rugs/', views.arearugsmain, name='arearugsmain'),

    #-Layer 2 Carpet Pages-#
    path('carpet-cleaning/', views.carpetcleaning, name='carpetcleaning'),
    path('carpet-cleaning/pet-stain-odor-treatment/', views.petstain, name='petstain'),
    path('carpet-stretching/', views.carpetstretching, name='carpetstretching'),
    path('carpet-repair/', views.carpetrepair, name='carpetrepair'),
    path('commercial-carpet-cleaning/', views.commercialcarpetcleaning, name='commercialcarpetcleaning'),
    path('advanced-spot-treatment/', views.advancedspot, name='advancedspot'),
    path('carpet-protector/', views.carpetprotector, name='carpetprotector'),

    #-Layer 2 Tile Pages-#
    path('tile-and-grout-cleaning/', views.tilegroutcleaning, name='tilegroutcleaning'),
    path('grout-sealing/', views.groutsealing, name='groutsealing'),
    path('grout-recoloring/', views.groutrecoloring, name='groutrecoloring'),
    path('grout-repair/', views.groutrepair, name='groutrepair'),
    path('commercial-tile-cleaning/', views.commercialtile, name='commercialtile'),
    path('tile-floor-slip-reduction/', views.tileslipreduction, name='tileslipreduction'),

    #-Layer 2 Upholstery Pages-#
    path('upholstery-cleaning-services/', views.upholsterycleaning, name='upholsterycleaning'),
    path('upholstery-repair/', views.upholsteryrepair, name='upholsteryrepair'),
    path('upholstery-protector/', views.upholsteryprotector, name='upholsteryprotector'),
    path('upholstery-pet-stain-odor/', views.uphpetstain , name='uphpetstain'),
    path('leather-cleaning-and-protector/', views.leathercleaning, name='leathercleaning'),
    path('auto-cleaning/', views.autocleaning, name='autocleaning'),

    #-Layer 2 Stone Pages-#
    path('stone-floor-cleaning/', views.stonefloorcleaning, name='stonefloorcleaning'),
    path('stone-honing-polishing-restoration/', views.stonehonepolish , name='stonehonepolish'),
    path('stone-sealers/', views.stonesealers, name='stonesealers'),
    path('granite-countertops/', views.granitecountertops, name='granitecountertops'),
    path('marble-travertine-limestone/', views.mtl, name='mtl'),
    path('stone-backsplash-cleaning-and-sealing/', views.stonebacksplash, name='stonebacksplash'),
    path('stone-repair/', views.stonerepair, name='stonerepair'),
    path('commercial-stone-care/', views.commercialstone, name='commercialstone'),
    path('stone-floor-slip-reduction/', views.stoneslipreduction, name='stoneslipreduction'),

    #-Layer 2 Area Rug Pages-#
    path('area-rug-cleaning/', views.arearugcleaning, name='arearugcleaning'),
    path('area-rug-repair/', views.arearugrepair, name='arearugrepair'),

    ##Other Pages##
    path('stay-beautiful-club/', views.staybeautiful, name='staybeautiful'),
    path('service-area/', views.servicearea, name='servicearea'),
    path('commercial-services/', views.commericalservices, name='commercialservices'),
    path('water-damage-extraction/', views.waterdamage, name='waterdamage'),
    #path('commercial-service-directory/', views.commercialdirectory),
    path('pricing/', views.pricing, name='pricing'),
    path('careers/', views.careers, name='careers'),
    path('meet-our-team/', views.meetourteam, name='meetourteam'),
    path('about-us/privacy-policy/', views.privacypolicy, name='privacypolicy'),

    ## City Pages ##
    path('the-woodlands-tx-carpet-cleaning/', views.thewoodlandscitypage, name='thewoodlandscitypage'),
    path('atascocita-tx-carpet-cleaning/', views.atascocitacitypage, name='atascocitacitypage'),

    ## DUPES ##
    path('stone-floor-and-countertop-care/', views.stonemain , name='stonemain2'),
    path('about-us/', views.whychooseus, name='whychooseus2'),
    path('contact/', views.booknow, name='booknow2'),
    path('carpet-stretching-and-repair/', views.repairmain, name='repairmain2'),


    ## THIS HAS TO BE LAST##
    #-Blog Functionality-#
    path('admin/', admin.site.urls),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    ##THIS HAS TO BE LAST##
]