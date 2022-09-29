from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=255, null=False, blank=False)
    item_desc=models.CharField(max_length=255, null=False, blank=False)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500, default="https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png")

    def __str__(self) -> str:
        return self.item_name
