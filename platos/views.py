from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .datos import platos


@api_view(['GET'])
def estado(request):
    return Response({"app": "Cafetería UTLA", "version": "1.0"})


@api_view(['GET'])
def lista_platos(request):
    return Response(platos)


@api_view(['GET'])
def detalle_plato(request, id):
    for plato in platos:
        if plato["id"] == id:
            return Response(plato)
    return Response({"error": "Plato no encontrado"}, status=status.HTTP_404_NOT_FOUND)