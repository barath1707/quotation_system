from django import forms
from .models import CustomerDetails, CustomerQuotation, QuotationTableInstance, QuotationTableHeader, QuotationTableValue, CustomerQuotationDetails, TableHeaderType

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['customer_name']

class QuotationForm(forms.ModelForm):
    class Meta:
        model = CustomerQuotation
        fields = ['quotation_name']

class QuotationTableForm(forms.ModelForm):
    class Meta:
        model = QuotationTableInstance
        fields = ['table_name']

class TableHeaderForm(forms.ModelForm):
    field_type = forms.ModelChoiceField(queryset=TableHeaderType.objects.all(),empty_label = 'Select' ,   required=True ,widget=forms.Select())
    class Meta:
        model = QuotationTableHeader
        fields = ['field_type','field_name']

class TableValueForm(forms.ModelForm):
    class Meta:
        model = QuotationTableValue
        fields = ['field_value']

class TableValueForm(forms.ModelForm):
    class Meta:
        model=QuotationTableHeader
        fields= ()
        
    def __init__(self, tableId,tableRowId,datalists,*args, **kwargs):
        super(TableValueForm, self).__init__(*args, **kwargs)
        IsoFlds = QuotationTableHeader.objects.filter(table_id=tableId)
        for loopCount,IsoFields in enumerate(IsoFlds):
            field_name = '%s' % (IsoFields.field_name,)
            hidfield_name = '%s' % (IsoFields.id,)
            self.fields[hidfield_name] = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control isoHiddenDynamicName', 'id': "dynamichidden"+str(loopCount) }),required = False,initial=IsoFields.id) 
            if IsoFields.field_type_id == 1:
                self.fields[field_name] = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete':'off','class': 'form-control isoDynamicName '+str(field_name),'inputmode':'none', 'id': "dynamic"+str(loopCount)  ,'data-field-id':IsoFields.id }))
            elif IsoFields.field_type_id == 2:
                self.fields[field_name] = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete':'off','class': 'form-control isoDynamicName numberinput'+str(field_name),'inputmode':'none', 'id': "dynamic"+str(loopCount)  ,'data-field-id':IsoFields.id }))
            elif IsoFields.field_type_id == 3:
                self.fields[field_name] = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete':'off','class': 'form-control isoDynamicName numberinput '+str(field_name),'inputmode':'none', 'id': "dynamic"+str(loopCount)  ,'data-field-id':IsoFields.id }))
            elif IsoFields.field_type_id == 4:
                self.fields[field_name] = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete':'off','class': 'form-control isoDynamicName datetimepicker '+str(field_name),'inputmode':'none', 'id': "dynamic"+str(loopCount)  ,'data-field-id':IsoFields.id }))
            self.fields[field_name].label = IsoFields.field_name
            if not datalists:
                dynamicobj = QuotationTableValue.objects.filter(field_id = IsoFields.id,row_id=tableRowId)
                if dynamicobj.exists():
                    self.initial[field_name] = dynamicobj[0].field_value
                else:
                    self.initial[field_name] = ""

from ckeditor.widgets import CKEditorWidget

class CustomerQuotationDetailsForm(forms.ModelForm):
    quotation_address = forms.CharField(widget=CKEditorWidget())
    quotation_subject = forms.CharField(widget=CKEditorWidget())
    quotation_description = forms.CharField(widget=CKEditorWidget())
    quotation_referrence = forms.CharField(widget=CKEditorWidget())
    quotation_note = forms.CharField(widget=CKEditorWidget())
    quotation_bank_details = forms.CharField(widget=CKEditorWidget())
    quotation_signature = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = CustomerQuotationDetails
        fields = [
            'quotation_date', 'quotation_address', 'quotation_subject',
            'quotation_description', 'quotation_referrence', 'quotation_note',
            'quotation_bank_details', 'quotation_signature'
        ]