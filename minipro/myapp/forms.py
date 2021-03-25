class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class InternProfileForm(forms.ModelForm):
    class Meta:
        model = InternProfile
        fields = ('location', 'bio')
        
class HRProfileForm(forms.ModelForm):
    class Meta:
        model = HRProfile
        fields = ('company_name', 'website')
class CEOProfileForm(forms.ModelForm):
    class Meta:
        model = CEOProfile
        fields = ('CEO_name')
class ProjectleadProfileForm(forms.ModelForm):
    class Meta:
        model = ProjectleadProfile
        fields = ('lead_name','lead_project')
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ('emp_name','emp_project')
