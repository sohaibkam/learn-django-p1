from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def Home(request):
    boards=Board.objects.all()
    # board_names=list()
    # for board in boards:
    #     board_names.append(str(board))
    #response_html = '<br>'.join(board_names)
    return render(request, 'home.html', {'boards': boards})