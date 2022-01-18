'''by spookyahell'''

import json

class TSV2JSONConverter(object):
	def __init__(self, file_path):
		self.file = open(file_path)
		self.fpath = file_path

#~ mode allows for a list and dict(ionary) version of the data 
	def convert(self, mode = 'dict', needle = 2):
		if mode == 'dict':
			result = {}
			data = self.file.read()
			lines = data.split('\n')
			data_titles = lines[0].split('\t')
			for idx, item in enumerate(lines):
				if item.strip() == '':
					continue
				indiv_res = {}
				if idx>0:
					datas = item.split('\t')
					for idx_d, data in enumerate(datas):
						if idx_d>0:
							indiv_res[data_titles[idx_d]] = datas[idx_d]
					if not datas[0] in result:
						result[datas[0]] = indiv_res
					else:							
						if type(result[datas[0]]) is list:
							result[datas[0]].append(indiv_res)
						else:
							result[datas[0]] = [result[datas[0]], indiv_res ]
							
		return json.dumps(result, indent = 2)