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
    province = request.GET.get("province", None)
    if year is None or year == '' or province is None or province == '':
        return para_error()
    province_id = find_keys_by_value(province_data, province)[0]
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


def add_air_data(request):
    data = json.loads(request.body.decode('utf-8'))
    year = data['year']
    print(year)
    data_list = data['list']
    for d in data_list:
        print(d)
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
            print(datas.aggregate(Avg('aqi')))
            average_aqi = datas.aggregate(Avg('aqi'))['aqi__avg']
            print(average_aqi)
            YearData.objects.create(year=year,
                                    province_id=province_id,
                                    average_aqi=average_aqi)
    return success_respond()


def find_keys_by_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]
