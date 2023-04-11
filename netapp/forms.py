from django import forms
from netapp.models import Nerecords,PErecords

# create a form to add ne record
class AddNeForm(forms.ModelForm):
    ne_type = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE Type","class":"form-control"}),label="")
    ne_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE Name",'class':'form-control'}),label="")
    ne_ip = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE IP",'class':'form-control'}),label="")
    aggreate_pe = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"Aggregating PE",'class':'form-control'}),label="")
    carrier_vlan_internet = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"Internet Carrier Vlan",'class':'form-control'}),label="")
    carrier_vlan_mpls = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"MPLS Carrier Vlan,if not available use internet Carrier",'class':'form-control'}),label="")
    pe_interface = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"PE Interface",'class':'form-control'}),label="")
    device_interfaces = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE intefaces",'class':'form-control'}),label="")
    comments =forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"comment",'class':'form-control'}),label="")
    
    class Meta:
        model=Nerecords
        fields = "__all__"


