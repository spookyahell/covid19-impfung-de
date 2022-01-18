from tsv2json import TSV2JSONConverter
import json



c = TSV2JSONConverter(r'tsv\germany_vaccinations_by_state.tsv')
res = c.convert()
with open('json\germany_vaccinations_by_state.json','w') as f:
	f.write(res)
	
	
c = TSV2JSONConverter(r'tsv\germany_vaccinations_timeseries_v2.tsv')
res = c.convert()
with open('json\germany_vaccinations_timeseries_v2.json','w') as f:
	f.write(res)



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
	
for day in delivery_timeseries:
	day_data = delivery_timeseries[day]
	delivery_timeseries_new[day] = []
	for entry in day_data:
		vacc_in_day = find_vaccine_in_day(entry['impfstoff'], day)
		if vacc_in_day > -1:
			vacc_o = delivery_timeseries_new[day][vacc_in_day]
			delivery_timeseries_new[day][vacc_in_day]['region_dosen'][entry['region']] = entry['dosen']
		else:
			delivery_timeseries_new[day].append({'impfstoff': entry['impfstoff'], 'region_dosen':{}})
			vacc_in_day = find_vaccine_in_day(entry['impfstoff'], day)
			delivery_timeseries_new[day][vacc_in_day]['region_dosen'][entry['region']] = entry['dosen']
			
with open('json\germany_deliveries_timeseries_v2.json','w') as f:
	f.write(json.dumps(delivery_timeseries_new, indent = 2))