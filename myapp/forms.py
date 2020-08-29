from django import forms

choice_day = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')]
choice_month = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')]
choice_year = [('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')]

class SampleForm(forms.Form):
    first_name=forms.CharField(max_length=20,required=True,label="First Name",widget=forms.TextInput(attrs={'placeholder':"First Name"}),help_text="Note: Space and Spl characters are not allowed")
    last_name=forms.CharField(max_length=20,required=True,label="Last Name",widget=forms.TextInput(attrs={'placeholder':"Last Name"}),help_text="Note: Space and Spl characters are not allowed")
    email=forms.EmailField(max_length=30,required=True,label="Email",widget=forms.TextInput(attrs={'placeholder':"Email"}),help_text="Note: abc@xyz.com")
    phno=forms.CharField(max_length=10,min_length=10,required=True,label="Phone Number",widget=forms.TextInput(attrs={'placeholder':"Phone Number",'pattern':'[6-9]\r{9}'}),help_text="No country codes")
    pwd=forms.CharField(max_length=20,required=True,label="Password",widget=forms.PasswordInput(attrs={'placeholder':"Password"}))
    birth_day=forms.ChoiceField(choices=choice_day,required=True,label="Birthday")
    birth_month=forms.ChoiceField(choices=choice_month,required=True,label="Birth Month")
    birth_year=forms.ChoiceField(choices=choice_year,required=True,label="Birth Year")
    gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female')],required=True,label="Gender",widget=forms.RadioSelect(attrs={'placeholder':"Gender"}))

