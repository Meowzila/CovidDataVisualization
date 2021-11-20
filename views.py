from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubmissionFormUS, SubmissionFormEU
from .QueryHandler import BuildQueryUS, BuildQueryEU
from .GenerateFigure import GenerateFigureUS, GenerateFigureEU
import chart_studio
import chart_studio.tools as tls
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('PLT_USER')
api_key = os.getenv('PLT_KEY')
tls.set_credentials_file(username=username, api_key=api_key)


def HomePage(request):
	return render(request, 'home.html')


def EU_Data(request):
	if request.method == 'POST':
		form = SubmissionFormEU(request.POST or None)
		if form.is_valid():
			level = form.cleaned_data.get('level')
			param = form.cleaned_data.get('param')
			normalized = form.cleaned_data.get('normalized')
			country = form.cleaned_data.get('country')
			region = form.cleaned_data.get('region')
			actual_latest = form.cleaned_data.get('actual_latest')
			date = form.cleaned_data.get('date')

			print(f'Level: {level}\nParameter: {param}\nNormalized: {normalized}\nCountry: {country}\nRegion: {region}\nDate: {date}\n')
			query = BuildQueryEU(level, param, country, region, date, actual_latest)
			query[param] = query[param].abs()
			print(f'{query}\n')
			GenerateFigureEU(level, query, param, country, normalized)

			defaults = {
			'level':'country', 
			'param':'new_confirmed', 
			'normalized':False,
			'country':'AL', 
			'region':['BLR', 'BGR', 'CZE', 'HUN', 'POL', 'MDA', 'ROU', 'RUS', 'SVK', 'UKR'],
			'actual_latest':False,
			'date':None}
			
			form = SubmissionFormEU(defaults, initial=defaults)
			print(f'Form has changed: {form.has_changed()}')
			if form.has_changed():
				new_form = {'level': level, 'param':param, 'normalized':normalized, 'country':country, 'region':region, 'actual_latest':actual_latest, 'date':date}
				form = SubmissionFormEU(new_form)
			else:
				new_form = {'form': form}
		return render(request, 'EU.html', {'form': form})

	default_form = SubmissionFormEU()
	return render(request, 'EU.html', {'form': default_form})


def US_Data(request):
	if request.method == 'POST':
		form = SubmissionFormUS(request.POST or None)
		if form.is_valid():
			level = form.cleaned_data.get('level')
			param = form.cleaned_data.get('param')
			normalized = form.cleaned_data.get('normalized')
			state = form.cleaned_data.get('state')
			region = form.cleaned_data.get('region')
			date = form.cleaned_data.get('date')

			print(f'Level: {level}\nParameter: {param}\nNormalized: {normalized}\nState: {state}\nRegion: {region}\nDate: {date}\n')
			query = BuildQueryUS(level, param, state, region, date)
			query[param] = query[param].abs()
			print(f'{query}\n')
			GenerateFigureUS(level, query, param, state, normalized)
	
			defaults = {
			'level':'county', 
			'param':'new_confirmed', 
			'normalized':False, 
			'state':'AK', 
			'region':['US_CT', 'US_ME', 'US_MA', 'US_NH', 'US_RI', 'US_VT', 'US_DE', 'US_NJ', 'US_NY', 'US_PA'],
			'date':None}
			
			form = SubmissionFormUS(defaults, initial=defaults)
			print(f'Form has changed: {form.has_changed()}')
			if form.has_changed():
				new_form = {'level': level, 'param':param, 'normalized':normalized, 'state':state, 'region':region, 'date':date}
				form = SubmissionFormUS(new_form)
			else:
				new_form = {'form': form}
		return render(request, 'US.html', {'form': form})

	default_form = SubmissionFormUS()
	return render(request, 'US.html', {'form': default_form})
