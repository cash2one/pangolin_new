from django.contrib import admin
from product.models import *
from embed_video.admin import AdminVideoMixin
from mptt.admin import MPTTModelAdmin
from product.fields import AdminImageWidget
from easy_thumbnails.fields import ThumbnailerImageField


# Register your models here.




class ProductAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ["product_title", "product_creator", "product_video", 'video_published', "product_date", "slogan", 'short_text',
              'full_text', 'slug',
              "product_tag", "product_category", 'published', 'ordering', 'published_main']

   
    list_filter = ["product_title", "product_date", "product_tag", "product_category", "product_creator", 'published']
    search_fields = ["product_title", "product_date", "product_tag", "product_category", "product_creator"]
    list_display = ["product_title", "product_category", "product_creator", 'published', 'ordering', 'published_main', 'pic_slug']
    list_editable = ['published', 'ordering', 'published_main']
    formfield_overrides = {
        ThumbnailerImageField: {'widget': AdminImageWidget},
    }


class  CategoryAdmin(admin.ModelAdmin):
      # fields = ['name', 'parent']
      list_display = ['name', 'parent', 'published', 'ordering']
      list_editable = ['published', 'ordering']


class  CreatorAdmin(admin.ModelAdmin):
      list_display = ['name', 'pic_slug']      



# class  WorksAdmin(admin.ModelAdmin):
#     # fields = ['work_creator', 'work_title', 'slug', 'short_text']    
#     list_filter = ['work_category', 'work_creator', 'work_title']  
#     search_fields = ['work_category','work_creator', 'work_title']  
#     list_display = ['work_title', 'work_category', 'work_creator', 'pic_slug', 'short_text']    
#     formfield_overrides = {
#         ThumbnailerImageField: {'widget': AdminImageWidget},
#     }


# class SlideAdmin(admin.ModelAdmin):
#     list_display = ['name', 'pic_slug', 'category', 'published', 'published_main', 'ordering']
#     list_editable = ['published','ordering', 'published_main']
#     formfield_overrides = {
#         models.ImageField: {'widget': AdminImageWidget},
    # }

   

# admin.site.register(Slide, SlideAdmin)        
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Tag)
# admin.site.register(Works, WorksAdmin)
