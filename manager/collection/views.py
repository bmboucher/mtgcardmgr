# from django.shortcuts import render
from collection.mtgmodels import Cards, Sets
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.db.models import QuerySet

# Create your views here.
def sets(request: HttpRequest):
    return JsonResponse({
        set.mtgocode: set.name for set in 
        Sets.objects.using('mtgjson').exclude(mtgocode=None).all()
    })

def cards(request: HttpRequest):
    startName = request.GET.get('startName', None)
    endName = request.GET.get('endName', None)
    setCode = request.GET.get('set', None)
    number = request.GET.get('number', None)

    queryset: QuerySet[Cards] = Cards.objects.using('mtgjson')
    if startName:
        queryset = queryset.filter(name__gte=startName)
    if endName:
        queryset = queryset.filter(name__lt=endName)
    if setCode:
        if setCode.endswith('*'):
            queryset = queryset.filter(setcode__startswith=setCode[:-1])
        else:
            queryset = queryset.filter(setcode=setCode)
    if number:
        if number.endswith('*'):
            queryset = queryset.filter(number__startswith=number[:-1])
        else:
            queryset = queryset.filter(number=number)
    if queryset.count() > 20:
        queryset = queryset[:10]
    return JsonResponse({
        'cards': [{
            "name": card.name,
            "scryfallId": card.scryfallid,
            "setCode": card.setcode,
            "number": card.number,
            "cardKingdomId": card.cardkingdomid,
            "cardKingdomFoilId": card.cardkingdomfoilid,
            "cardKingdomEtchedId": card.cardkingdometchedid
        } for card in queryset]})