from django.shortcuts import render, redirect

def index(request):
	return render(request, 'surveyFormTemp/index.html')


def formProcess(request):
	if 'counter' in request.session:
		request.session['counter'] +=1
	else:
		request.session['counter'] = 1

	request.session['data'] = {
		'name': request.POST['f_name'],
		'dojoLocation': request.POST['dojoLocation'],
		'favLang': request.POST['favlang'],
		'comments': request.POST['comments'],
	}

	return redirect('/showResults')

def showResults(request):
	print 'Got to show results'
	print request.session
	return render(request, 'surveyFormTemp/results.html')


