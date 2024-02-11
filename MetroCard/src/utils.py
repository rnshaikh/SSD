


def format_params(row):

	ans = []
	for param in row:
		param = param.strip()
		try:
			param = int(param)
			ans.append(param)
		except:
			if param:
				ans.append(param)
	return ans