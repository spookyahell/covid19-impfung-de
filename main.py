# by @spookyahell -- License: MIT

import json
import sys, locale, platform

from copy import copy
from os.path import isfile
from os import sep
from datetime import datetime
from subprocess import call

import requests

from tsv2json import TSV2JSONConverter

# Deutsch, bitte!
system = platform.system()
if system == 'Windows':
	locale.setlocale(locale.LC_ALL, 'deu_deu')
else:
	locale.setlocale(locale.LC_ALL, 'de_DE')



# Wir prüfen zuallererst, ob es bei der Webseite selbst Änderungen gegeben hat
# Die Methode dafür: Größe der Seite überprüfen, bei Abweichung von mehr als 10 bytes, abbrechen
r = requests.get('https://impfdashboard.de/daten')

if isfile('impfdaten-hash'):
	# Bei Vorhandensein eines vorherigen Hashes der Datenseite, den Hash kurz verifizieren
	with open('impfdaten-length') as f:
		jso = json.loads(f.read())
		length = jso['length']
	
	
	diff = length(r.content) - length
	if (diff > 5) or (diff < -5):
		print(f'''Ehrr... oops, site has changed. (Previous length was {length}, now it's {len(r.content)})
It's good policy to check the details of those changes first. Aborting.''')
		sys.exit(1)
	else:
		print('Verified by length. Site has not changed.')
	
else:
	#Bei fehlen der letzten Größe und die HTML im Verzeichnis speichern
	with open('impfdaten.html', 'wb') as f:
		f.write(r.content)
	with open('impfdaten-length','w') as f:
		f.write(json.dumps({'length':len(r.content)}))
		


# Download der Originaldaten von impfdashboard.de
base = 'https://impfdashboard.de/static/data/'

meta = 'metadata.json'

r = requests.get(base+meta)
vaccinationsLastUpdated = r.json()['vaccinationsLastUpdated']

stand_str = datetime.strptime(vaccinationsLastUpdated,'%Y-%m-%d %H:%M:%S').strftime('Stand: %d. %B %Y, %H:%M Uhr')

if isfile('stand'):
	with open('stand') as f:
		last_stand = f.read()
else:
	last_stand = None
		
if stand_str != last_stand:
	print('New data available, will now download, convert & commit...')
	with open('stand','w') as f:
		f.write(stand_str)
else:
	print('FEHLER: Es sind noch keine neuen Daten verfügbar.\nSpäter gerne erneut probieren')
	sys.exit(2)

filenames = ['germany_deliveries_timeseries_v2.tsv',
	'germany_vaccinations_timeseries_v2.tsv',
	'germany_vaccinations_by_state.tsv']

for filename in filenames:
	print(f'Downloading {filename!r} from impfdashboard.de...', end = '', flush = True)
	r = requests.get(base+filename)
	with open(f'tsv{sep+filename}', 'wb') as f:
		f.write(r.content)
	print('OK.')

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
	
print('ALL CONVERSIONS COMPLETED!')

call(['cnp.cmd', stand_str])