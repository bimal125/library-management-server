from django.db import models


class MetaInformation(models.Model):
    # Add common fields here
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(MetaInformation):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")
        ordering = ['-id', ]

    def __str__(self):
        return self.first_name


class Category(MetaInformation):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        ordering = ['-id', ]

    def __str__(self):
        return self.name


class Book(MetaInformation):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    author = models.ForeignKey("Author", on_delete=models.PROTECT)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
        ordering = ['-id', ]

    def __str__(self):
        return self.name
