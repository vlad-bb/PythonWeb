from .app import *


def get_exc():
    api_client = ApiClient(RequestConnection(requests))
    data_xml = api_client.get_xml(
        'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    print(f' Actual course 1 USD = { parse_course(xml_adapter, data_xml) } UAH')

new = get_exc()