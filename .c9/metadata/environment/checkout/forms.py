{"filter":false,"title":"forms.py","tooltip":"/checkout/forms.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":25,"column":9},"action":"remove","lines":["  ","from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"],"id":2},{"start":{"row":0,"column":0},"end":{"row":24,"column":9},"action":"insert","lines":["from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"]}],[{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["A"],"id":3}],[{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"remove","lines":["A"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":24,"column":9},"action":"remove","lines":["from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"],"id":5},{"start":{"row":0,"column":0},"end":{"row":24,"column":9},"action":"insert","lines":["from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":24,"column":9},"end":{"row":24,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1595184145412,"hash":"1ac3e6136c20827cc78f75e42ed39b668a81f44d"}