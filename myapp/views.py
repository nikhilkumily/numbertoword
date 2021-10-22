from django.shortcuts import render
from django.views.generic import View, TemplateView
from num2words import num2words
# Create your views here.

class Home(TemplateView):
    print("her")
    template_name = "home_1.html"
    def get(self, request):
        return render(request,self.template_name)
    def post(self, request):
        if (request.method == 'POST'):
            number = request.POST.get('number')
            print(number)
            try:
                if int(number) >= 0 and int(number)<=1000000:
                   message = num2words(int(number))
                   message = "Number in words is: " + (str(message)).upper()
                elif int(number) <= 0:
                    message = "Entered number is too low, please enter a positive number"
                elif int(number)>=1000000:
                     message = "Entered number is too high"
            except TypeError as e:
                message = "Enter a valid number"
            except Exception as e:
                print("exce",e)
                message = "Enter a valid number"
                print("mes",message)
            return render(request,self.template_name, {'number': number, "message":message})