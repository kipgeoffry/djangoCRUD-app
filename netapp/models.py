from django.db import models

# Create your models here.
class Nerecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ne_type = models.CharField(max_length=50)
    ne_name = models.CharField(max_length=50)
    ne_ip = models.CharField(max_length=15)
    aggreate_pe = models.CharField(max_length=50)
    carrier_vlan_internet = models.IntegerField()
    carrier_vlan_mpls = models.IntegerField()
    pe_interface = models.CharField(max_length=50)
    device_interfaces = models.CharField(max_length=50,null=True)
    comments =models.CharField(max_length=100,null=True)

    def __str__(self):
        return {self.ne_type}
    
class PErecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    pe_model = models.CharField(max_length=40)
    pe_name = models.CharField(max_length=50)
    pe_ip1 = models.CharField(max_length=15)
    pe_ip2 = models.CharField(max_length=15,null=True)
    pe_interface1 = models.CharField(max_length=50)
    pe_interface2 = models.CharField(max_length=50,null=True)
    pe_interface3 = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f" {self.pe_model} {self.pe_name} {self.pe_ip1} {self.pe_ip2}"
    
