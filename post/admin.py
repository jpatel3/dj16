from django.contrib import admin
from post.models import Post, Comments

class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 3

class PostAdmin(admin.ModelAdmin):
	list_display = ('content', 'pub_date', 'was_published_recently')
	search_fields = ['content']
	list_filter = ['pub_date']
	inlines = [CommentsInline]

admin.site.register(Post, PostAdmin)