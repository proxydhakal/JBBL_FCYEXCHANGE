from django.db import models
from import_export import resources

class Branches(models.Model):
    BranchName = models.CharField(max_length=255)
    BranchCode = models.CharField(max_length=10)
    Status = models.CharField(max_length=20)
    EmailStatus = models.CharField(max_length=20)
    EmailAddress = models.CharField(max_length=255)
    RegionalBranchName = models.CharField(max_length=255, null=True, blank=True)
    IsEnteredBy = models.CharField(max_length=255, null=True, blank=True)
    IsEnteredDate = models.CharField(max_length=255, null=True, blank=True)
    IsEditedBy = models.CharField(max_length=255, null=True, blank=True)
    IsEditedDate = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.BranchCode}"  # Display a meaningful representation of the object

    class Meta:
        verbose_name = "BRANCHES"
        verbose_name_plural = "BRANCHES"

class BranchesResource(resources.ModelResource):
    class Meta:
        model = Branches