import home.models
from Django import utils

def make_graph():
    temperature_graph = dict()
    lines=dict()
    max_datas,min_datas = dict(),dict()
    for temperature in home.models.Temperature.objects.all():
        print(temperature.date)
        pub_date = utils.date2unixtime(temperature.date)
        print(pub_date,temperature.max_temperature,temperature.min_temperature)
        max_datas[pub_date] = temperature.max_temperature
        min_datas[pub_date] = temperature.min_temperature
    lines['max'] = max_datas
    lines['min'] = min_datas
    temperature_graph['data'] = lines
    return temperature_graph

なんかグラフが変