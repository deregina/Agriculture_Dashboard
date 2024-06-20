from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Cc2019, Cc2020, Cc2021, Cc2022, Cc2023])
admin.site.register([Cv2019, Cv2020, Cv2021, Cv2022, Cv2023])
admin.site.register([Ecv2019, Ecv2020, Ecv2021, Ecv2023])
admin.site.register([Exg2019, Exg2020, Exg2021, Exg2022, Exg2023])
admin.site.register([Ph2019, Ph2020, Ph2021, Ph2022, Ph2023])
admin.site.register([Yield2019, Yield2020, Yield2021, Yield2022, Yield2023])
admin.site.register([Shp2019, Shp2022])
admin.site.register([Cc2022_shp])