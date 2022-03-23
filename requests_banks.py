import requests
from bs4 import BeautifulSoup
import datetime
import json

#Requests
def call_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def ge_state_rates():
	soup = call_url('https://nbg.gov.ge/en/monetary-policy/currency')
	span = soup.find_all('span', class_='text-body1 font-normal font-md leading-body1 text-grey-800')
	state_usd_sell = float(span[-6].text.replace(',', '.'))
	state_euro_sell = float(span[26].text.replace(',', '.'))
	state_lira_sell = float(span[-10].text.replace(',', '.'))
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'state', 'country': 'gel',
				   'usd_sell': state_usd_sell, 'usd_buy': None, 'euro_sell': state_euro_sell, 'euro_buy': None,
				   'lira_sell': state_lira_sell, 'lira_buy': None}
	return result_dict
	
def ge_rico_rates():
	soup = call_url('https://www.rico.ge/')
	span = soup.find_all('td', class_='h5 font-weight-bold text-primary')
	rico_usd_sell = float(span[0].text.strip())
	rico_usd_buy = float(span[1].text.strip())
	rico_euro_sell = float(span[2].text.strip())
	rico_euro_buy = float(span[3].text.strip())
	rico_lira_sell = float(span[10].text.strip())
	rico_lira_buy = float(span[11].text.strip())
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'rico', 'country': 'gel', 'usd_sell': rico_usd_sell,
				   'usd_buy': rico_usd_buy, 'euro_sell': rico_euro_sell, 'euro_buy': rico_euro_buy,
				   'lira_sell': rico_lira_sell, 'lira_buy': rico_lira_buy}
	return result_dict
	
	
def ge_tbc_rates():
	soup = call_url('https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangeratessmall_WAR_tbcpwexchangeratessmallportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-5&p_p_col_count=1')
	soup_lira = call_url('https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=allRatesTab&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=3')
	tbc_usd_sell = float(soup.find_all('div', class_='currRate')[0].text.strip())
	tbc_usd_buy = float(soup.find_all('div', class_='currRate')[1].text.strip())
	tbc_euro_sell = float(soup.find_all('div', class_='currRate')[2].text.strip())
	tbc_euro_buy = float(soup.find_all('div', class_='currRate')[3].text.strip())
	tbc_lira_sell = float(soup_lira.find_all('span', class_='currCopyAll')[-2].text.strip())
	tbc_lira_buy = float(soup_lira.find_all('span', class_='currCopyAll')[-1].text.strip())
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'tbc', 'country': 'gel', 'usd_sell': tbc_usd_sell,
				   'usd_buy': tbc_usd_buy, 'euro_sell': tbc_euro_sell, 'euro_buy': tbc_euro_buy,
				   'lira_sell': tbc_lira_sell, 'lira_buy': tbc_lira_buy}
	return result_dict

def ge_georgiabank_rates():
	soup = call_url('https://bankofgeorgia.ge/api/currencies/page/pages/5c0a361ff85d2d574073cf30')
	json_obj = json.loads(soup.text)
	geo_usd_sell = float(json_obj['data']['tabs'][0]['tabContent']['currenciesList'][0]['buyRate'])
	geo_usd_buy = float(json_obj['data']['tabs'][0]['tabContent']['currenciesList'][0]['sellRate'])
	geo_euro_sell = float(json_obj['data']['tabs'][0]['tabContent']['currenciesList'][1]['buyRate'])
	geo_euro_buy = float(json_obj['data']['tabs'][0]['tabContent']['currenciesList'][1]['sellRate'])
	geo_lira_sell = float(json_obj['data']['tabs'][0]['tabContent']['currenciesList'][5]['buyRate'])
	geo_lira_buy = float(json_obj['data']['tabs'][0]['tabContent']['currenciesList'][5]['sellRate'])
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'georgia', 'country': 'gel', 'usd_sell': geo_usd_sell,
				   'usd_buy': geo_usd_buy, 'euro_sell': geo_euro_sell, 'euro_buy': geo_euro_buy,
				   'lira_sell': geo_lira_sell, 'lira_buy': geo_lira_buy}
	return result_dict


def ge_mbc_rates():
	soup = call_url(
		'https://fxrates.mbc.com.ge:8022/api/fxrates/mbc/commercial?fbclid=IwAR0YnhhhQgvHblGe06uyIwQmyv4s8ngxTjZInSVlTKvKNcMZshPdaoydFfo/api/fxrates/mbc/commercial')
	json_obj = json.loads(soup.text)
	mbc_usd_sell = float(json_obj['FXRates'][4]['Buy'])
	mbc_usd_buy = float(json_obj['FXRates'][4]['Sell'])
	mbc_euro_sell = float(json_obj['FXRates'][0]['Buy'])
	mbc_euro_buy = float(json_obj['FXRates'][0]['Sell'])
	mbc_lira_sell = float(json_obj['FXRates'][3]['Buy'])
	mbc_lira_buy = float(json_obj['FXRates'][3]['Sell'])
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'mbc', 'country': 'gel', 'usd_sell': mbc_usd_sell,
				   'usd_buy': mbc_usd_buy, 'euro_sell': mbc_euro_sell, 'euro_buy': mbc_euro_buy,
				   'lira_sell': mbc_lira_sell, 'lira_buy': mbc_lira_buy}
	return result_dict


def ge_basis_rates():
	soup = call_url('https://static.bb.ge/source/api/view/main/getXrates')
	json_obj = json.loads(json.loads(soup.text)[0]['xrates'])
	basis_usd_sell = float(json_obj['kursBuy']['USD'])
	basis_usd_buy = float(json_obj['kursSell']['USD'])
	basis_euro_sell = float(json_obj['kursBuy']['EUR'])
	basis_euro_buy = float(json_obj['kursSell']['EUR'])

	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'basis', 'country': 'gel', 'usd_sell': basis_usd_sell,
				   'usd_buy': basis_usd_buy, 'euro_sell': basis_euro_sell, 'euro_buy': basis_euro_buy,
				   'lira_sell': None, 'lira_buy': None}
	return result_dict


def ge_crystal_rates():
	soup = call_url('https://crystal.ge/exchange')
	currencies = soup.find_all('tr')
	crystal_usd_sell = float(currencies[1].text.strip()[7:14])
	crystal_usd_buy = float(currencies[1].text.strip()[14:20])
	crystal_euro_sell = float(currencies[2].text.strip()[7:14])
	crystal_euro_buy = float(currencies[2].text.strip()[14:20])
	crystal_lira_sell = float(currencies[4].text.strip()[7:14])
	crystal_lira_buy = float(currencies[4].text.strip()[14:20])
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'crystal', 'country': 'gel', 'usd_sell': crystal_usd_sell,'usd_buy': crystal_usd_buy, 'euro_sell': crystal_euro_sell, 'euro_buy': crystal_euro_buy,'lira_sell': crystal_lira_sell, 'lira_buy': crystal_lira_buy}
	return result_dict


def ge_credo_rates():
    soup = call_url('https://credobank.ge/')
    currencies_buy = soup.find_all('div', class_="currency second-column")
    currencies_sell = soup.find_all('div', class_="third-column")
    credo_usd_sell = float(currencies_buy[0].text)
    credo_usd_buy = float(currencies_sell[0].text)
    credo_euro_sell = float(currencies_buy[1].text)
    credo_euro_buy = float(currencies_sell[1].text)
    result_dict = {'day': datetime.date.today(), 'name_bank': 'credo', 'country': 'gel', 'usd_sell': credo_usd_sell,'usd_buy': credo_usd_buy, 'euro_sell': credo_euro_sell, 'euro_buy': credo_euro_buy,'lira_sell': None, 'lira_buy': None}
    return result_dict


def ru_tinkoff_rates():
	soup_usd = call_url('https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB')
	json_obj = json.loads(soup_usd.text)
	tinkoff_usd_sell = float(json_obj['payload']['rates'][0]['buy'])
	tinkoff_usd_buy = float(json_obj['payload']['rates'][0]['sell'])
	soup_euro = call_url('https://api.tinkoff.ru/v1/currency_rates?from=EUR&to=RUB')
	json_obj = json.loads(soup_euro.text)
	tinkoff_euro_sell = float(json_obj['payload']['rates'][0]['buy'])
	tinkoff_euro_buy = float(json_obj['payload']['rates'][0]['sell'])
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'tinkoff', 'country': 'rub', 'usd_sell': tinkoff_usd_sell,
				   'usd_buy': tinkoff_usd_buy, 'euro_sell': tinkoff_euro_sell, 'euro_buy': tinkoff_euro_buy,
				   'lira_sell': None, 'lira_buy': None}
	return result_dict


def tr_isbank_rates():
	soup = call_url('https://www.isbank.com.tr/en/foreign-exchange-rates')
	currencies = soup.find_all('tr')
	is_usd_sell = float(currencies[1].text.strip().replace('\n', '').replace('\r', '').replace(' ', '').replace(',', '.')[17:23])
	is_usd_buy = float(currencies[1].text.strip().replace('\n', '').replace('\r', '').replace(' ', '').replace(',', '.')[24:30])
	is_euro_sell = float(currencies[2].text.strip().replace('\n', '').replace('\r', '').replace(' ', '').replace(',', '.')[7:13])
	is_euro_buy = float(currencies[2].text.strip().replace('\n', '').replace('\r', '').replace(' ', '').replace(',', '.')[14:20])
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'is_bank', 'country': 'try', 'usd_sell': is_usd_sell,'usd_buy': is_usd_buy, 'euro_sell': is_euro_sell, 'euro_buy': is_euro_buy,'lira_sell': None, 'lira_buy': None}
	return result_dict


def tr_trabzon_rates():
	soup = call_url('https://www.beyazdoviz.com/')
	currencies = soup.find_all('tr')
	trabzon_usd_sell = float(currencies[1].text.strip()[18:24])
	trabzon_usd_buy = float(currencies[1].text.strip()[25:31])
	trabzon_euro_sell = float(currencies[2].text.strip()[21:27])
	trabzon_euro_buy = float(currencies[2].text.strip()[28:34])
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'trabzon', 'country': 'try', 'usd_sell': trabzon_usd_sell,'usd_buy': trabzon_usd_buy, 'euro_sell': trabzon_euro_sell, 'euro_buy': trabzon_euro_buy,'lira_sell': None, 'lira_buy': None}
	return result_dict


def by_prior_rates():
	soup = call_url('https://www.prior.by/web/Bia.Portlets.Mc.Default.CurrencyRates.Prior.Widget/RatesWidget/Index?prtlId=prtl3&controller=&view=&title=&_=1647252095591')
	currencies = soup.find_all('div', class_="new")
	prior_usd_sell = float(currencies[0].text.strip())
	prior_usd_buy = float(currencies[1].text.strip())
	prior_euro_sell = float(currencies[6].text.strip())
	prior_euro_buy = float(currencies[7].text.strip())
	result_dict = {'day': datetime.date.today().strftime("%d-%m-%Y"), 'name_bank': 'prior', 'country': 'byn', 'usd_sell': prior_usd_sell,'usd_buy': prior_usd_buy, 'euro_sell': prior_euro_sell, 'euro_buy': prior_euro_buy,'lira_sell': None, 'lira_buy': None}
	return result_dict




