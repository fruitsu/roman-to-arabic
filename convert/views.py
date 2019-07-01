from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
import json
from .models import roman_numerals, roman_lit
import re


def start(request):
    if request.method == "POST":
        return JsonResponse(convertRequest(request.POST["value"]), safe=False)
    elif request.method == "GET":
        return render(request, "convert/base.html")


def convertRequest(input_number):
    range_flag = ""
    input_number = str(input_number).replace(" ", "").upper()
    if input_number.isdigit():
        input_number = int(input_number)
        if input_number > 3999:
            return 'Dura lex sed lex: числа больше 3999 вводить нельзя'
        if input_number < 0:
            return 'Dura lex sed lex: отрицательные числа вводить нельзя'
        for num, lit in roman_numerals:
            while input_number >= num:
                range_flag += lit
                input_number -= num
    elif re.fullmatch("[IVXLCDM]+", input_number):
        if any(num * 4 in input_number for num in ['I', 'X', 'C', 'M']):
            return "Dura lex sed lex: нельзя писать больше 3-х {} подряд".format(input_number)
        if any(num * 2 in input_number for num in ['V', 'L', 'D']):
            return "Dura lex sed lex: нельзя писать больше 2-х {} подряд".format(input_number)

        range_flag = int()
        maxNum = 1
        for ch in input_number[::-1]:
            curNum = roman_lit[ch]
            if curNum >= maxNum:
                range_flag += curNum
                maxNum = curNum
            else:
                range_flag -= curNum
    return range_flag
