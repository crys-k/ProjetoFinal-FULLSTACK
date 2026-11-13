from django.shortcuts import render, redirect
from .models import Funcionario
from .forms import FuncionarioForm
from django.db.models import queue
from django.db.models.functions import Lower
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



    
    