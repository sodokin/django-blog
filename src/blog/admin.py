from django.contrib import admin
from .models import BlogPost
# On peut aussi enregistrer la table sous forme de class en faisant:


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "created_on",
        "last_updated",
    )
    list_editable = ("published",)


admin.site.register(BlogPost, BlogPostAdmin)
