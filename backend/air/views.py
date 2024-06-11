import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import AirData, YearData
from backend.lib.static_res import *
from backend.lib.province import province_data
from backend.lib.month import months
from django.db.models import Avg


# Create your views here.
def get_average_aqi(request):
    year = request.GET.get('year', None)
    print(year)

    if year is None or year == '':
        return para_error()
    data = YearData.objects.filter(year=year).all()
    if data.count() == 0:
        return para_error()
    province_list = []
    for province in data:
        p_id = province.province_id
        province_list.append({
            'province': province_data.get(p_id),
            'province_id': p_id,
            'average_aqi': "{:.2f}".format(province.average_aqi)
        })
    return JsonResponse({
        'province_list': province_list
    })


def get_aqi(request):
    year = request.GET.get("year", None)
    province_id = request.GET.get("province_id", None)
    if year is None or year == '' or province_id is None or province_id == '':
        return para_error()
    data = AirData.objects.filter(year=year, province_id=province_id).all()
    if data.count() == 0:
        return para_error()
    month_list = []
    for month in range(1, 13):
        month_data = data.filter(month=month).first()
        month_list.append({
            'month': month,
            'aqi': "{:.2f}".format(month_data.aqi)
        })
    return JsonResponse({
        'month_list': month_list
    })


def get_pollutants(request):
    year = request.GET.get("year", None)
    province_id = request.GET.get("province_id", None)
    if year is None or year == '' or province_id is None or province_id == '':
        return para_error()
    data = AirData.objects.filter(year=year, province_id=province_id).all()
    if data.count() == 0:
        return para_error()
    month_list = []
    for month in range(1, 13):
        month_data = data.filter(month=month).first()
        month_list.append({
            'month': find_keys_by_value(months, month)[0],
            'PM2_5': "{:.2f}".format(month_data.pm25),
            'PM10': "{:.2f}".format(month_data.pm10),
            'SO2': "{:.2f}".format(month_data.so2),
            'NO2': "{:.2f}".format(month_data.no2),
            'O3': "{:.2f}".format(month_data.o3)
        })
    return JsonResponse({
        'month_list': month_list
    })


def get_pollutant(request):
    year = request.GET.get("year", None)
    pollutant_id = request.GET.get("pollutant_id", None)
    if year is None or year == '' or pollutant_id is None or pollutant_id == '':
        return para_error()
    data = YearData.objects.filter(year=year).all()
    if data.count() == 0:
        return para_error()
    print(data)
    print(pollutant_id)
    if pollutant_id == '0':
        list = data.order_by('-average_pm25')
    elif pollutant_id == '1':
        list = data.order_by('-average_pm10')
    elif pollutant_id == '2':
        list = data.order_by('-average_so2')
    elif pollutant_id == '3':
        list = data.order_by('-average_no2')
    elif pollutant_id == '4':
        list = data.order_by('-average_co')
    elif pollutant_id == '5':
        list = data.order_by('-average_o3')
    else:
        return para_error()
    city_list = []
    for d in list:
        if pollutant_id == '0':
            value = d.average_pm25
        elif pollutant_id == '1':
            value = d.average_pm10
        elif pollutant_id == '2':
            value = d.average_so2
        elif pollutant_id == '3':
            value = d.average_no2
        elif pollutant_id == '4':
            value = d.average_co
        else:
            value = d.average_o3
        city_list.append({
            'cityName': province_data.get(d.province_id),
            'value': value
        })
    return JsonResponse({
        'city_list': city_list
    })


def add_air_data(request):
    data = json.loads(request.body.decode('utf-8'))
    year = data['year']
    data_list = data['list']
    for d in data_list:
        province_id = find_keys_by_value(province_data, d['province'])[0]
        AirData.objects.create(year=year,
                               month=months.get(d['month']),
                               province_id=province_id,
                               aqi=d['AQI'],
                               pm25=d['PM2.5(微克每立方米)'],
                               pm10=d['PM10(微克每立方米)'],
                               so2=d['SO2(微克每立方米)'],
                               no2=d['NO2(微克每立方米)'],
                               co=d['CO(毫克每立方米)'],
                               o3=d['O3(微克每立方米)'],
                               u=d['U(m/s)'],
                               v=d['V(m/s)'],
                               temp=d['TEMP(K)'],
                               rh=d['RH(%)'],
                               psfc=d['PSFC(Pa)'])
    return success_respond()


def add_year_data(request):
    for year in range(2013, 2019):
        for province_id in range(1, 34):
            print(f'year:{year},province_id:{province_id}')
            datas = AirData.objects.filter(year=year, province_id=province_id).all()
            print(datas)
            average_aqi = datas.aggregate(Avg('aqi'))['aqi__avg']
            print(f'aqi:{average_aqi}')
            average_pm25 = datas.aggregate(Avg('pm25'))['pm25__avg']
            print(f'pm25:{average_pm25}')
            average_pm10 = datas.aggregate(Avg('pm10'))['pm10__avg']
            print(f'pm10:{average_pm10}')
            average_so2 = datas.aggregate(Avg('so2'))['so2__avg']
            print(f'so2:{average_so2}')
            average_no2 = datas.aggregate(Avg('no2'))['no2__avg']
            print(f'no2:{average_no2}')
            average_co = datas.aggregate(Avg('co'))['co__avg']
            print(f'co:{average_co}')
            average_o3 = datas.aggregate(Avg('o3'))['o3__avg']
            print(f'o3:{average_o3}')
            YearData.objects.create(year=year,
                                    province_id=province_id,
                                    average_aqi=average_aqi,
                                    average_pm25=average_pm25,
                                    average_pm10=average_pm10,
                                    average_so2=average_so2,
                                    average_no2=average_no2,
                                    average_co=average_co,
                                    average_o3=average_o3)
    return success_respond()


def find_keys_by_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]
