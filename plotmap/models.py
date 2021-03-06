from django.db import models


# Create your models here.
class State(models.Model):
    state = models.CharField('State', max_length=50, null=True)

    def __str__(self):
        return self.state


class District(models.Model):
    district = models.CharField('District', max_length=50, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    id_state = models.IntegerField('State ID', null=True)

    def __str__(self):
        return self.district


class ItemCode(models.Model):
    ItemCode = models.IntegerField('Item Code', null=True)
    id_district = models.IntegerField('District ID', null=True)

    def __str__(self):
        return str(self.ItemCode)


class Item(models.Model):
    Item = models.CharField('Item', max_length=50, null=True)
    ItemCode = models.ForeignKey(ItemCode, on_delete=models.CASCADE, null=True)
    id_itemcode = models.IntegerField('Item Code', blank=True, null=True)

    def save(self, **kwargs):

        self.id_itemcode = "%d" % self.ItemCode_id
        super(Item, self).save(**kwargs)

    def __str__(self):
        return self.Item

class DepartmentContactDetails(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    ItemCode = models.ForeignKey(ItemCode, on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=30, null=True)
    departmentName = models.CharField('Department Name', max_length=100, null=True)
    departmentAddress = models.CharField('Department Address', max_length=100, null=True)
    contactperson = models.CharField('Contact Person', max_length=100, null=True)
    contactno = models.CharField('Contact No', max_length=20, null=True)
    contactEmail = models.EmailField('Contact Email', null=True)

    def __str__(self):
        return self.departmentName

    class Meta:
        verbose_name = "Department Contact Detail"
        verbose_name_plural = "Department Contact Details"

class ItemDescription(models.Model):
    departmentContactDetails = models.ForeignKey(DepartmentContactDetails, on_delete=models.CASCADE, null=True)
    item_desc = models.CharField('Item Description', max_length=200, null=True)
    location = models.CharField('Location', max_length=50, null=True)
    item_live_location_source = models.CharField('Item Live Location Source', max_length=40, null=True)
    last_updation = models.DateField('Last Updation', null=True)

    def __str__(self):
        return self.item_desc

    class Meta:
        verbose_name = "Item Description"
        verbose_name_plural = "Item Descriptions"


