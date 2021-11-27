from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class SubmissionFormUS(forms.Form):
	level = forms.ChoiceField(choices=[
		('county', 'By County'), 
		('state', 'By State'),
		('region', 'By Region'),  
		('country', 'By Country')])

	param = forms.ChoiceField(choices=[
		('new_confirmed', 'New Confirmed Cases'), 
		('cumulative_confirmed', 'Total Confirmed Cases'),
		('new_deceased', 'New Deaths'), 
		('cumulative_deceased', 'Total Deaths'),
		('new_persons_fully_vaccinated', 'New Fully Vaccinated'),
		('cumulative_persons_fully_vaccinated', 'Total Fully Vaccinated'),
		('population', 'Population')])

	normalized = forms.BooleanField(required=False, initial=False, label='Normalize per 100,000 People (State/Region/Country)')

	state = forms.ChoiceField(choices=[('AK', 'AK'), 
		('AL', 'AL'), ('AR', 'AR'), ('AZ', 'AZ'), ('CA', 'CA'), ('CO', 'CO'),
 		('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'),
 		('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'),
		('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'),
 		('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MS', 'MS'),
 		('MT', 'MT'), ('NC', 'NC'), ('ND', 'ND'), ('NE', 'NE'), ('NH', 'NH'),
 		('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('OH', 'OH'),
 		('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), 
 		('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VA', 'VA'),
 		('VT', 'VT'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY')], required=False)

	region = forms.ChoiceField(choices=[
		(['US_CT', 'US_ME', 'US_MA', 'US_NH', 'US_RI', 'US_VT', 'US_DE', 'US_NJ', 'US_NY', 'US_PA'], 'Northeast'),
		(['US_CT', 'US_ME', 'US_MA', 'US_NH', 'US_RI', 'US_VT'], 'Northeast: New England'),
		(['US_DE', 'US_NJ', 'US_NY', 'US_PA'], 'Northeast: Mid-Atlanic'), 
		(['US_IL', 'US_IN', 'US_MI', 'US_OH', 'US_WI', 'US_IA', 'US_KS', 'US_MN', 'US_MO', 'US_NE', 'US_ND', 'US_SD'], 'Midwest'),
		(['US_IL', 'US_IN', 'US_MI', 'US_OH', 'US_WI'], 'Midwest: East North Central'),
		(['US_IA', 'US_KS', 'US_MN', 'US_MO', 'US_NE', 'US_ND', 'US_SD'], 'Midwest: West North Central'),
		(['US_DC', 'US_FL', 'US_GA', 'US_MD', 'US_NC', 'US_SC', 'US_VA', 'US_WV', 'US_AL', 'US_KY', 'US_MS', 'US_TN', 'US_AR', 'US_LA', 'US_OK', 'US_TX'], 'South'),
		(['US_DC', 'US_FL', 'US_GA', 'US_MD', 'US_NC', 'US_SC', 'US_VA', 'US_WV'], 'South: South Atlantic'),
		(['US_AL', 'US_KY', 'US_MS', 'US_TN'], 'South: East South Central'),
		(['US_AR', 'US_LA', 'US_OK', 'US_TX'], 'South: West South Central'),
		(['US_AZ', 'US_CO', 'US_ID', 'US_MT', 'US_NV', 'US_NM', 'US_UT', 'US_WY', 'US_CA', 'US_OR', 'US_WA'], 'West'),
		(['US_AZ', 'US_CO', 'US_ID', 'US_MT', 'US_NV', 'US_NM', 'US_UT', 'US_WY'], 'West: Mountain'),
		(['US_CA', 'US_OR', 'US_WA'], 'West: Pacific')], 
		required=False)

	date = forms.DateField(label='Specific Date (YYYY-MM-DD)', 
		required=False, 
		input_formats=['%Y-%m-%d'], 
		help_text='(OPTIONAL) Default: Latest')


class SubmissionFormEU(forms.Form):
	level = forms.ChoiceField(choices=[
		('country', 'By Country'), 
		('region', 'By Region')])

	param = forms.ChoiceField(choices=[
		('new_confirmed', 'New Confirmed Cases'), 
		('cumulative_confirmed', 'Total Confirmed Cases'),
		('new_deceased', 'New Deaths'), 
		('cumulative_deceased', 'Total Deaths'),
		('new_persons_fully_vaccinated', 'New Fully Vaccinated'),
		('cumulative_persons_fully_vaccinated', 'Total Fully Vaccinated'),
		('population', 'Population')])

	normalized = forms.BooleanField(required=False, initial=False, label='Normalize per 100,000 People')

	country = forms.ChoiceField(choices=[
		('ALB', 'Albania'), ('AND', 'Andorra'), ('ARM', 'Armenia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'),
 		('BLR', 'Belarus'), ('BEL', 'Belgium'), ('BIH', 'Bosnia and Herzegovina'), ('BGR', 'Bulgaria'), ('HRV', 'Croatia'),
 		('CYP', 'Cyprus'), ('CZE', 'Czechia'), ('DNK', 'Denmark'), ('EST', 'Estonia'), ('FIN', 'Finland'),
		('FRA', 'France'), ('GEO', 'Georgia'), ('DEU', 'Germany'), ('GRC', 'Greece'), ('HUN', 'Hungary'),
 		('ISL', 'Iceland'), ('IRL', 'Ireland'), ('ITA', 'Italy'), ('KAZ', 'Kazakhstan'), ('RKS', 'Kosovo'),
 		('LVA', 'Latvia'), ('LIE', 'Liechtenstein'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('MLT', 'Malta'),
 		('MDA', 'Moldova'), ('MCO', 'Monaco'), ('MNE', 'Montenegro'), ('NLD', 'Netherlands'), ('MKD', 'North Macedonia'),
 		('NOR', 'Norway'), ('POL', 'Poland'), ('PRT', 'Portugal'), ('ROU', 'Romania'), ('RUS', 'Russia'), 
 		('SMR', 'San Marino'), ('SRB', 'Serbia'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('ESP', 'Spain'),
 		('SWE', 'Sweden'), ('CHE', 'Switzerland'), ('TUR', 'Turkey'), ('UKR', 'Ukraine'), ('GBR', 'United Kingdom'),
 		('VAT', 'Vatican City')])
	
	region = forms.ChoiceField(choices=[
		(['BLR', 'BGR', 'CZE', 'HUN', 'POL', 'MDA', 'ROU', 'RUS', 'SVK', 'UKR'], 'Eastern Europe'),
		(['DNK', 'EST', 'FIN', 'ISL', 'IRL', 'LVA', 'LTU', 'NOR', 'SWE', 'GBR'], 'Northern Europe'),
		(['ALB', 'AND', 'BIH', 'HRV', 'GRC', 'VAT', 'ITA', 'MLT', 'MNE', 'MKD', 'PRT', 'SMR', 'SRB', 'SVN', 'ESP'], 'Southern Europe'), 
		(['AUT', 'BEL', 'FRA', 'DEU', 'LIE', 'LUX', 'MCO', 'NLD', 'CHE'], 'Western Europe'),
		(['BLR', 'BGR', 'CZE', 'HUN', 'POL', 'MDA', 'ROU', 'RUS', 'SVK', 'UKR', 
		  'DNK', 'EST', 'FIN', 'ISL', 'IRL', 'LVA', 'LTU', 'NOR', 'SWE', 'GBR',
		  'ALB', 'AND', 'BIH', 'HRV', 'GRC', 'VAT', 'ITA', 'MLT', 'MNE', 'MKD', 
		  'PRT', 'SMR', 'SRB', 'SVN', 'ESP', 'AUT', 'BEL', 'FRA', 'DEU', 'LIE', 
		  'LUX', 'MCO', 'NLD', 'CHE'], 'All of Europe')],
		required=False)

	date = forms.DateField(label='Specific Date (YYYY-MM-DD)', 
		required=False, 
		input_formats=['%Y-%m-%d'], 
		help_text='(OPTIONAL) Default: Latest EU Data ~3 days ago')


class MovingAverageForm(forms.Form):
	level = forms.ChoiceField(choices=[
	('state', 'By State'), 
	('country', 'Entire Country')])

	param = forms.ChoiceField(choices=[
	('new_confirmed', 'New Confirmed Cases'), 
	('new_deceased', 'New Deaths'), 
	('new_persons_fully_vaccinated', 'New Fully Vaccinated')])

	state = forms.ChoiceField(choices=[('AK', 'AK'), 
	('AL', 'AL'), ('AR', 'AR'), ('AZ', 'AZ'), ('CA', 'CA'), ('CO', 'CO'),
	('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'),
	('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'),
	('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'),
	('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MS', 'MS'),
	('MT', 'MT'), ('NC', 'NC'), ('ND', 'ND'), ('NE', 'NE'), ('NH', 'NH'),
	('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('OH', 'OH'),
	('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), 
	('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VA', 'VA'),
	('VT', 'VT'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY')], required=False)

	start_date = forms.DateField(label='Start Date (YYYY-MM-DD)', 
	required=False, 
	input_formats=['%Y-%m-%d'], 
	help_text='(OPTIONAL) Default: 2020-01-01')

	end_date = forms.DateField(label='End Date (YYYY-MM-DD)', 
	required=False, 
	input_formats=['%Y-%m-%d'], 
	help_text='(OPTIONAL) Default: Today')