from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubmissionFormUS, SubmissionFormEU, MovingAverageForm
from .QueryHandler import BuildQueryUS, BuildQueryEU, MovingAverageQuery
from .GenerateFigure import GenerateFigureUS, GenerateFigureEU, GenerateFigureMovingAverage
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
			date = form.cleaned_data.get('date')

			print(f'Level: {level}\nParameter: {param}\nNormalized: {normalized}\nCountry: {country}\nRegion: {region}\nDate: {date}\n')
			query = BuildQueryEU(level, param, country, region, date)
			query[param] = query[param].abs()
			print(f'{query}\n')
			GenerateFigureEU(level, query, param, country, normalized)

			defaults = {
			'level':'country', 
			'param':'new_confirmed', 
			'normalized':False,
			'country':'AL', 
			'region':['BLR', 'BGR', 'CZE', 'HUN', 'POL', 'MDA', 'ROU', 'RUS', 'SVK', 'UKR'],
			'date':None}
			
			form = SubmissionFormEU(initial=defaults)
			print(f'Form has changed: {form.has_changed()}')
			if form.has_changed():
				new_form = {'level': level, 'param':param, 'normalized':normalized, 'country':country, 'region':region, 'date':date}
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
			
			form = SubmissionFormUS(initial=defaults)
			print(f'Form has changed: {form.has_changed()}')
			if form.has_changed():
				new_form = {'level': level, 'param':param, 'normalized':normalized, 'state':state, 'region':region, 'date':date}
				form = SubmissionFormUS(new_form)
			else:
				new_form = {'form': form}
		return render(request, 'US.html', {'form': form})

	default_form = SubmissionFormUS()
	return render(request, 'US.html', {'form': default_form})


def Moving_Average(request):
	if request.method == 'POST':
		form = MovingAverageForm(request.POST or None)
		if form.is_valid():
			level = form.cleaned_data.get('level')
			param = form.cleaned_data.get('param')
			state = form.cleaned_data.get('state')
			start_date = form.cleaned_data.get('start_date')
			end_date = form.cleaned_data.get('end_date')

			print(f'Level: {level}\nParameter: {param}\nState: {state}\nStart Date: {start_date}\nEnd Date: {end_date}')
			query = MovingAverageQuery(level, param, state, start_date, end_date)
			query[param] = query[param].abs()
			print(f'{query}\n')
			GenerateFigureMovingAverage(query, level, param, state, start_date, end_date)
	
			defaults = {
			'level':'state', 
			'param':'new_confirmed', 
			'state':'AK', 
			'start_date':None,
			'end_date':None}
			
			form = MovingAverageForm(initial=defaults)
			print(f'Form has changed: {form.has_changed()}')
			if form.has_changed():
				new_form = {'level': level, 'param':param, 'state':state, 'start_date':start_date, 'end_date':end_date}
				form = MovingAverageForm(new_form)
			else:
				new_form = {'form': form}
		return render(request, 'average.html', {'form': form})

	default_form = MovingAverageForm()
	return render(request, 'average.html', {'form': default_form})