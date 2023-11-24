from django.db import models
from import_export import resources

class FCYRateMaster(models.Model):
   
    date =models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    user = models.CharField(blank=False, null=False,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.date} - {self.time}"
    
    class Meta:
        verbose_name = "FCY RATE MASTER"
        verbose_name_plural = "FCY RATE MASTERS"
    

class FCYExchangeRate(models.Model):
    masterid      = models.IntegerField()
    currency_code = models.CharField(max_length=10)
    currency = models.CharField(max_length=255)
    currency_unit = models.CharField(max_length=50)
    buying_rate_deno_50_or_less = models.DecimalField(max_digits=10, decimal_places=2)
    buying_rate_deno_50_or_above = models.DecimalField(max_digits=10, decimal_places=2)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=2)
    premium_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.currency_code} - {self.currency_unit}"
    
    class Meta:
        verbose_name = "FCY EXCHANGE RATE"
        verbose_name_plural = "FCY EXCHANGE RATES"
    
class CurrencyTable(models.Model):
    cyc_code = models.CharField(max_length=10)
    cyc_desc = models.CharField(max_length=255)
    cyc_desc_long = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cyc_desc} - {self.cyc_desc_long}"
    class Meta:
        verbose_name = "CURRENCY TABLE"
        verbose_name_plural = "CURRENCY TABLES"
        
class CurrencyTableResource(resources.ModelResource):
    class Meta:
        model = CurrencyTable


class FCYExchangeRequestMaster(models.Model):
    refrenceid          = models.CharField(max_length=20, unique=True)  
    date                = models.DateField()
    preferredBranch     = models.CharField(max_length=10, null=False, blank=False)  
    totalEquivalentNPR  = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)  
    totalEquivalentNPRToWords = models.CharField(max_length=300, null=False, blank=False)  
    status              = models.CharField(max_length=50, null=False, blank=False)
    remarks             = models.TextField(default='-')
    enteredBy           = models.CharField(max_length=255)  
    enterDate           = models.DateTimeField()
    updatedBy           = models.CharField(max_length=255)  
    updateDate          = models.DateTimeField()
    deletedBy           = models.CharField(max_length=255)  
    deletedDate         = models.DateTimeField()

    def __str__(self):
        return f"{self.refrenceid} - {self.date} - {self.preferredBranch}"  
    

    def save(self, *args, **kwargs):
        
        if not self.refrenceid:  
            prefix = "JBBL-FCY-"  
            
            latest_id = FCYExchangeRequestMaster.objects.filter(refrenceid__startswith=prefix).order_by('-refrenceid').first()
            if latest_id:
                last_id_number = int(latest_id.refrenceid[len(prefix):])
            else:
                last_id_number = 0
            new_id_number = last_id_number + 1
            self.refrenceid = f"{prefix}{new_id_number:07}" 
        super(FCYExchangeRequestMaster, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "FCY EXCHANGE REQUEST MASTER TABLE"
        verbose_name_plural = "FCY EXCHANGE REQUEST MASTER TABLES"

class FCYDenoMasterTable(models.Model):
    masterid        = models.IntegerField()
    currency        = models.CharField(max_length=255)  
    deno            = models.IntegerField()
    unit            = models.IntegerField()
    rate            = models.DecimalField(max_digits=20, decimal_places=2)
    equivalentNPR   = models.DecimalField(max_digits=20, decimal_places=2)  
    status          = models.CharField(max_length=50)  
    enteredBy       = models.CharField(max_length=255)  
    enterDate       = models.DateTimeField()
    updatedBy       = models.CharField(max_length=255)  
    updateDate      = models.DateTimeField()
    deletedBy       = models.CharField(max_length=255)  
    deletedDate     = models.DateTimeField()

    def __str__(self):
        return f"{self.currency} - {self.deno}"  
    class Meta:
        verbose_name = "FCY DENO MASTER TABLE"
        verbose_name_plural = "FCY DENO MASTER TABLES"
