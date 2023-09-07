from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rest_framework.request import Request
from django.core.paginator import Paginator
from django.urls import reverse_lazy


def paginate_response(request:Request,serializer_class:ModelSerializer,per_page:int,data) -> Response:
    page = int(request.GET.get('page', 1))
    pagination = Paginator(object_list=data, per_page=per_page)
    results = serializer_class(pagination.page(page), many=True).data

    previous = None
    next = None

    if(page > 1):
        previous = reverse_lazy('liked') + f'?page={page - 1}' 
    if(page < pagination.num_pages):
        next = reverse_lazy('liked') + f'?page={page + 1}'

    return Response(
        {
            'results': results,
            'previous_page': previous,
            'next_page': next,
            'page': page, 
            'max_page': pagination.num_pages
        }, 
        status=status.HTTP_200_OK
    ) 


def paginate_response_with_filters(request:Request,serializer_class:ModelSerializer,per_page:int,data,filters:dict) -> Response:
    page = int(request.GET.get('page', 1))
    pagination = Paginator(object_list=data, per_page=per_page)
    results = serializer_class(pagination.page(page), many=True).data

    previous = None
    next = None
    
    date,to_oldest,string = filters
    date = filters[f'{date=}'.split('=')[0]]
    to_oldest = filters[f'{to_oldest=}'.split('=')[0]]
    string = filters[f'{string=}'.split('=')[0]]

    if(page > 1):
        previous = reverse_lazy('posts') + f'?string={string}&date={date}&to_oldest={to_oldest}&page={page - 1}' 
    if(page < pagination.num_pages):
        next = reverse_lazy('posts') + f'?string={string}&date={date}&to_oldest={to_oldest}&page={page + 1}'

    return Response(
        {
            'results': results,
            'previous_page': previous,
            'next_page': next,
            'page': page, 
            'max_page': pagination.num_pages
        }, 
        status=status.HTTP_200_OK
    )

