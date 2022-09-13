from django.contrib.sitemaps import Sitemap
from Deckers_Carpet_Cleaning_Site.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['deckersite:homepage', 'deckersite:whychooseus', 'deckersite:booknow', 'deckersite:servicedirectory', 'deckersite:carpetmain','deckersite:upholsterymain', 'deckersite:tilemain', 'deckersite:stonemain', 'deckersite:repairmain', 'deckersite:arearugsmain', 'deckersite:carpetcleaning', 'deckersite:petstain', 'deckersite:carpetstretching', 'deckersite:carpetrepair', 'deckersite:commercialcarpetcleaning', 'deckersite:advancedspot', 'deckersite:carpetprotector', 'deckersite:tilegroutcleaning', 'deckersite:groutsealing', 'deckersite:groutrecoloring', 'deckersite:groutrepair', 'deckersite:commercialtile', 'deckersite:tileslipreduction', 'deckersite:upholsterycleaning', 'deckersite:upholsteryrepair', 'deckersite:upholsteryprotector', 'deckersite:leathercleaning', 'deckersite:autocleaning', 'deckersite:stonefloorcleaning', 'deckersite:stonehonepolish', 'deckersite:stonesealers', 'deckersite:granitecountertops', 'deckersite:mtl', 'deckersite:stonebacksplash', 'deckersite:stonerepair', 'deckersite:commercialstone', 'deckersite:stoneslipreduction', 'deckersite:arearugcleaning', 'deckersite:arearugrepair', 'deckersite:staybeautiful', 'deckersite:servicearea', 'deckersite:commercialservices', 'deckersite:waterdamage', 'deckersite:pricing', 'deckersite:careers', 'deckersite:meetourteam', 'deckersite:privacypolicy', 'deckersite:thewoodlandscitypage', 'deckersite:atascocitacitypage', 'deckersite:kingwoodcitypage', 'deckersite:stonemain2', 'deckersite:whychooseus2', 'deckersite:booknow2', 'deckersite:repairmain2']
    def location(self, item):
        return reverse(item)