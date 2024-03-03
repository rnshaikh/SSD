import sys

TRAIN_PATH = {
	"TRAIN_A" : {
		"ENGINE": sys.maxsize,
		"CHN": 0,
		"SLM": 350,
		"BLR": 550,
		"KRN": 900,
		"HYB": 1200,
		"NGP": 1600,
		"ITJ": 1900,
		"BPL": 2000,
		"AGA": 2500,
		"NDL": 2700,
		"PTA": 3000,
		"NJP": 3400,
		"GHY": 3900
	},
	"TRAIN_B" : {
		"ENGINE": sys.maxsize,
		"TVC": 0,
		"SRR": 300,
		"MAQ": 600,
		"MAO": 1000,
		"PNE": 1400,
		"HYB": 2000,
		"NGP": 2400,
		"ITJ": 2700,
		"BPL": 2800,
		"AGA": 3300,
		"NDL": 3500,
		"PTA": 3800,
		"NJP": 4200,
		"GHY": 4700,
	},
	"TRAIN_AB": {
		"ENGINE": sys.maxsize,
		"NGP": 400,
		"ITJ": 700,
		"BPL": 800,
		"AGA": 1300,
		"NDL": 1500,
		"PTA": 1800,
		"NJP": 2200,
		"GHY": 2700,
	}
}
ENGINE='ENGINE'
INIT_ZERO=0
INIT_ONE=1
MERGE_STATION="HYB"
ARRIVAL="ARRIVAL"
DEPARTURE="DEPARTURE"
MERGE_TRAIN_NAME="TRAIN_AB"