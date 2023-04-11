from django import forms
from netapp.models import Nerecords,PErecords

# create a form to add ne record
class AddNeForm(forms.ModelForm):
    ne_type = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE Type","class":"form-control"}),label="")
    ne_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE Name",'class':'form-control'}),label="")
    ne_ip = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE IP",'class':'form-control'}),label="")
    aggreate_pe = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"Aggregating PE",'class':'form-control'}),label="")
    carrier_vlan_internet = forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"Internet Carrier Vlan",'class':'form-control'}),label="")
    carrier_vlan_mpls = forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"MPLS Carrier Vlan,if not available use internet Carrier",'class':'form-control'}),label="")
    pe_interface = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"PE Interface",'class':'form-control'}),label="")
    device_interfaces = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"NE intefaces",'class':'form-control'}),label="")
    comments =forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"comment",'class':'form-control'}),label="")
    
    class Meta:
        model=Nerecords
        fields = "__all__"
    #A form to add PE 
class AddPeForm(forms.ModelForm):
    pe_model = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"PE Type","class":"form-control"}),label="")
    pe_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"Name","class":"form-control"}),label="")
    pe_ip1 = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"PE 1 ip","class":"form-control"}),label="")
    pe_ip2 = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"PE 2 ip","class":"form-control"}),label="")
    pe_interface1 = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'Placeholder':"Interface 1","class":"form-control"}),label="")
    pe_interface2 = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"Interface 2","class":"form-control"}),label="")
    pe_interface3 = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'Placeholder':"Interface 3","class":"form-control"}),label="")
    
    class Meta:
        model=PErecords
        fields = "__all__"



