﻿from tsv2json import TSV2JSONConverter
import json
from copy import copy


c = TSV2JSONConverter(r'tsv\germany_vaccinations_by_state.tsv')
res = c.convert()
with open('json\germany_vaccinations_by_state.json','w') as f:
	f.write(res)
	
	
c = TSV2JSONConverter(r'tsv\germany_vaccinations_timeseries_v2.tsv')
res = c.convert()
with open('json\germany_vaccinations_timeseries_v2.json','w') as f:
	f.write(res)


# Tage mit Impfdaten zwecks besserer Nachverfolgbarkeit aufteilen nach Jahr&Monaten
vaccinations_timeseries = json.loads(res)
jahr_und_monat_ = None
monthly_json = {}
for day, day_data in vaccinations_timeseries.items():
	jahr_und_monat = '-'.join(day.split('-')[:-1])
	if jahr_und_monat != jahr_und_monat_:
		if jahr_und_monat_ != None:
			with open(f'json\germany_vaccinations_timeseries_v2_monthly\germany_vaccinations_timeseries_v2-{jahr_und_monat_}.json','w') as f:
				f.write(json.dumps(monthly_json, indent = 2))
			monthly_json = {}
	monthly_json[day] = day_data
	jahr_und_monat_ = copy(jahr_und_monat)
	
if len(monthly_json) > 0:
	#~ print('Writing the last file...')
	with open(f'json\germany_vaccinations_timeseries_v2_monthly\germany_vaccinations_timeseries_v2-{jahr_und_monat}.json','w') as f:
		f.write(json.dumps(monthly_json, indent = 2))
	

c = TSV2JSONConverter(r'tsv\germany_deliveries_timeseries_v2.tsv')
res = c.convert()


# Datenformat der Regierung für "Zeitreihe der bundesweiten Impfungen" suckt für 'smartes' JSON, da muss noch rumgefuschelt werden
delivery_timeseries = json.loads(res)

delivery_timeseries_new = {}
def find_vaccine_in_day(vname, day):
	for idx, list_item in enumerate(delivery_timeseries_new[day]):
		if vname == list_item['impfstoff']:
			return idx
	return -1
	
#~ def find_facility_in_deliveries(facility_name, facility_deliveries):
	
	
for day in delivery_timeseries:
	facility_data = {}
	day_data = delivery_timeseries[day]
	delivery_timeseries_new[day] = []
	if type(day_data) is dict:
		day_data = [day_data]
	for entry in day_data:
		if entry['einrichtung'] not in facility_data:
			facility_data[entry['einrichtung']] = {}
		vacc_in_day = find_vaccine_in_day(entry['impfstoff'], day)
		if not (vacc_in_day > -1):
			delivery_timeseries_new[day].append({'impfstoff': entry['impfstoff'], 'region_dosen':{}})
			vacc_in_day = find_vaccine_in_day(entry['impfstoff'], day)
		
		facility_data[entry['einrichtung']][entry['region']] = entry['dosen']
		delivery_timeseries_new[day][vacc_in_day]['region_dosen'] = facility_data
			
with open('json\germany_deliveries_timeseries_v2.json','w') as f:
	f.write(json.dumps(delivery_timeseries_new, indent = 2))
	#~ f.write(res)