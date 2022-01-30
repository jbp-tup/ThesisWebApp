from django.forms import ModelForm
from .models import MvnsCollectedData


class AddDataForm(ModelForm):
    class Meta:
        model = MvnsCollectedData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddDataForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['orderNumber'].label = 'Order Number'
        self.fields['officerName'].label = 'Officer Name'
        self.fields['motoristFirstName'].label = 'Motorist First Name'
        self.fields['motoristMiddleInitial'].label = 'Motorist Middle Initial'
        self.fields['motoristLastName'].label = 'Motorist Last Name'
        self.fields['plateNumber'].label = 'Vehicle Plate Number'
        self.fields['dbReading'].label = 'Decibel Reading'
        self.fields['distance'].label = 'Distance Reading'


class EditDataForm(ModelForm):
    class Meta:
        model = MvnsCollectedData
        fields = ['motoristFirstName', 'motoristMiddleInitial', 'motoristLastName']
