from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MembershipTypeService import MembershipTypeService
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def membership_type_index(request):

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    """
    types debe tener:
    id, name, guests, price, tipoCobro (billing) de tipo membresia
    """

    context = {
        'membershipTypes' : types,
    }

    return render(request, 'Admin/Membership/index_type_membership.html', context) 


@require_http_methods(['GET'])
def create_membership_type_index(request):

    context = {
        'titulo' : 'titulo'
    }
    
    return render(request, 'Admin/Membership/new_type_membership.html', context)

@require_http_methods(['POST'])
def edit_membership_type_index(request):

    membership_type_service = MembershipTypeService()

    typeId = request.POST['id']

    type = membership_type_service.getType(typeId)

    context = {
        'membershipType' : type,
    }

    return render(request, 'Admin/Membership/edit_type_membership.html', context)


@require_http_methods(['POST'])
def delete_membership_type(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    membership_type_service = MembershipTypeService()

    membership_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@require_http_methods(['POST'])
def create_membership_type(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["guests"] = request.POST['guests']

    insert_data["price"] = request.POST['price']

    insert_data["billing"] = request.POST['billing']

    insert_data["status"] = 1

    membership_type_service = MembershipTypeService()

    membership_type_service.create(insert_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@require_http_methods(['POST'])
def edit_membership_type(request):

    edit_data = {}

    edit_data["name"] = request.POST['name']

    edit_data["guests"] = request.POST['guests']

    edit_data["price"] = request.POST['price']

    edit_data["billing"] = request.POST['billing']

    id_edit = request.POST['id']

    membership_type_service = MembershipTypeService()

    membership_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))