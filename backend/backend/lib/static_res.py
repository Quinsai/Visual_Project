from django.http import JsonResponse


def success_respond():
    return JsonResponse({}, status=200)


def para_error():
    return JsonResponse({'reason': '请求参数错误'}, status=404)
