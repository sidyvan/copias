from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from datetime import date
import datetime
from django.contrib.auth import logout
from core.forms import CaixaForm, UserForm
from core.models import Caixa
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/entrar/")
def fechamento_de_caixa(request):
    lista =  Caixa.objects.all().order_by('-pk')[:40]
    return render(request, 'core/fechamento_de_caixa.html', {'lista':lista})

def logout_admin(request):
    logout(request)
    return redirect('home')

@login_required(login_url="/entrar/")
def remover_caixa(request, pk):
    c = get_object_or_404(Caixa, pk=pk)
    c.delete()
    return redirect('home')


@login_required(login_url="/entrar/")
def remover_caixa_resumo(request, pk):
    c = get_object_or_404(Caixa, pk=pk)
    c.delete()
    return redirect('resmo')


@login_required(login_url="/entrar/")
def resumo(request):

    if request.method == "POST":
        inicio = request.POST['data_inicio']
        fim = request.POST['data_final']
        if inicio == '' or fim == '':
            obj = Caixa.objects.all()
            copias = Caixa.objects.aggregate(total_copias=Sum('quantidade'))
            caixa = Caixa.objects.aggregate(total_caixa=Sum('valor_total'))
            lista_aux =  Caixa.objects.all().order_by('-pk')
            paginator = Paginator(lista_aux, 25)
            page = request.GET.get('page')
            try:
                lista = paginator.page(page)
            except PageNotAnInteger:
                lista = paginator.page(1)
            except EmptyPage:
                lista = paginator.page(paginator.num_pages)

            return render(request, 'core/resumo.html',{'copias':copias,'caixa':caixa,'lista':lista})
        else:

            obj = Caixa.objects.filter(criado_em__range=(inicio, fim))
            copias = Caixa.objects.filter(criado_em__range=(inicio, fim)).aggregate(total_copias=Sum('quantidade'))
            caixa = Caixa.objects.filter(criado_em__range=(inicio, fim)).aggregate(total_caixa=Sum('valor_total'))
            lista_aux =  Caixa.objects.filter(criado_em__range=(inicio, fim)).order_by('-pk')


            paginator = Paginator(lista_aux, 25)

            page = request.GET.get('page')
            try:
                lista = paginator.page(page)
            except PageNotAnInteger:
                lista = paginator.page(1)
            except EmptyPage:
                lista = paginator.page(paginator.num_pages)

            return render(request, 'core/resumo.html',{'obj':obj,'copias':copias,'caixa':caixa,'lista':lista, 'inicio':inicio, 'fim':fim})
    else:
        copias = Caixa.objects.aggregate(total_copias=Sum('quantidade'))
        caixa = Caixa.objects.aggregate(total_caixa=Sum('valor_total'))
        lista_aux = Caixa.objects.all().order_by('-pk')



        paginator = Paginator(lista_aux, 25)
        page = request.GET.get('page')
        try:
            lista = paginator.page(page)
        except PageNotAnInteger:
            lista = paginator.page(1)
        except EmptyPage:
            lista = paginator.page(paginator.num_pages)

        return render(request, 'core/resumo.html',{'copias':copias,'caixa':caixa,'lista':lista})

@login_required(login_url="/entrar/")
def home(request):
    lista =  Caixa.objects.all().order_by('-pk')[:10]
    #dia = Caixa.filter(data_date__date=date.today())
    form = CaixaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.valor_total = post.quantidade * post.preco.valor_copia
            post.autor = request.user
            post.save()
            return redirect('home')
    else:
        return render(request, 'core/home.html',  {'form': form, 'lista':lista})

def dashboard(request):

    return render(request, 'core/dashboard.html')

def entrar(request):
	form = UserForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')

			else:
				#return HttpResponseRedirect('/gerente/entrar/')
				context = {
					'form':form,
				}
				return render(request, 'core/login.html', context)
		else:
			pass
	else:
		context = {
			'form':form,
		}
		return render(request, 'core/login.html', context)
