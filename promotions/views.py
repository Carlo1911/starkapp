from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.PromotionsService import PromotionsService
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index(request):

    promotion_service = PromotionService()

    promotions = promotion_service.getPromotions()

    context = {
        'promotions' : promotions,
    }

    return render(request, 'Admin/Discounts/index_promotion.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    return render(request, 'Admin/Discounts/new_promotion.html', context)

@require_http_methods(['GET'])
def edit_index(request):

    promotion_service = PromotionService()

    promotion = promotion_service.getPromotion()

    context = {
        'promotion' : promotion,
    }

    return render(request, 'Admin/Discounts/edit_promotion.html', context)

@require_http_methods(['POST'])
def delete_promotion(request):

    insert_data = {}

    insert_data["id"] = request.POST['id']

    insert_data["estado"] = 0

    promotion_service = PromotionService()

    promotion_service.update(insert_data)

    return HttpResponseRedirect(reverse('promotions:index'))


@require_http_methods(['POST'])
def create_promotion(request):

    insert_data = {}

    insert_data["descripcion"] = request.POST['descripcion']

    insert_data["porcentaje"] = request.POST['porcentaje']

    insert_data["estado"] = 1

    promotion_service = PromotionService()

    promotion_service.create(insert_data)

    return HttpResponseRedirect(reverse('promotions:index'))


@require_http_methods(['POST'])
def edit_promotion(request):

    insert_data = {}

    insert_data["descripcion"] = request.POST['descripcion']

    insert_data["porcentaje"] = request.POST['porcentaje']

    insert_data["id"] = request.POST['id']

    promotion_service = PromotionService()

    promotion_service.update(insert_data)

    return HttpResponseRedirect(reverse('promotions:index'))