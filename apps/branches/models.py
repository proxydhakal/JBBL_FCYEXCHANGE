from django.db import models
from import_export import resources
from simple_history.models import HistoricalRecords

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
    history = HistoricalRecords()
    
    def __str__(self):
        return f"{self.BranchCode}"  # Display a meaningful representation of the object

    class Meta:
        verbose_name = "BRANCHES"
        verbose_name_plural = "BRANCHES"

class BranchesResource(resources.ModelResource):
    class Meta:
        model = Branches
        
class BranchTellorAccount(models.Model):
    CyCode = models.CharField(max_length=5)
    CyDesc = models.CharField(max_length=10)
    MainCode = models.CharField(max_length=20)
    Name = models.CharField(max_length=255)
    history = HistoricalRecords()
    
    def __str__(self):
        return f"{self.CyDesc}"  # Display a meaningful representation of the object

    class Meta:
        verbose_name = "BRANCH TELLOR ACCOUNT"
        verbose_name_plural = "BRANCH TELLOR ACCOUNT"
class BranchesTellorAccountResource(resources.ModelResource):
    class Meta:
        model = BranchTellorAccount