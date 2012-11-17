from xml.dom.minidom import parseString


def parse_xml(xml):
    with open(xml) as f:
        data = [line for line in f]
    return parseString(''.join(data))


def query_for_element(dom, elem):
    return dom.getElementsByTagName(elem)


def get_values(line, *args):
    return {arg: line.getAttribute(arg) for arg in args}


if __name__ == '__main__':
    a = parse_xml('/Users/Dan/Downloads/DailyTradeConfirm_Test.xml')
    b = query_for_element(a, 'TradeConfirm')
    for line in b:
        print(get_values(line,
                         'description','symbol', 'orderID', 'assetCategory',
                         'putCall', 'quantity', 'price', 'commission',
                         'dateTime', 'code', 'buySell'))