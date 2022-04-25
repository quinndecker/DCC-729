from django.contrib.sitemaps import Sitemap
from Deckers_Carpet_Cleaning_Site.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['homepage', 'whychooseus', 'booknow', 'servicedirectory', 'carpetmain','upholsterymain', 'tilemain', 'stonemain', 'repairmain', 'arearugsmain', 'carpetcleaning', 'petstain', 'carpetstretching', 'carpetrepair', 'commercialcarpetcleaning', 'advancedspot', 'carpetprotector', 'tilegroutcleaning', 'groutsealing', 'groutrecoloring', 'groutrepair', 'commercialtile', 'tileslipreduction', 'upholsterycleaning', 'upholsteryrepair', 'upholsteryprotector', 'leathercleaning', 'autocleaning', 'stonefloorcleaning', 'stonehonepolish', 'stonesealers', 'granitecountertops', 'mtl', 'stonebacksplash', 'stonerepair', 'commercialstone', 'stoneslipreduction', 'arearugcleaning', 'arearugrepair', 'staybeautiful', 'servicearea', 'commercialservices', 'waterdamage', 'pricing', 'careers', 'meetourteam', 'privacypolicy', 'thewoodlandscitypage', 'atascocitacitypage', 'stonemain2', 'whychooseus2', 'booknow2', 'repairmain2']
    def location(self, item):
        return reverse(item)