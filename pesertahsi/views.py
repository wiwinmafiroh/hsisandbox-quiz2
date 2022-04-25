from django.shortcuts import render
from django.http import HttpResponse
from pesertahsi.banksoal.banksoal import EvaluasiHarian
import random

# Create your views here.
def pesertahsi(request):
  bank_soal = EvaluasiHarian()
  jml_soal = 2
  soal_acak = random.sample(bank_soal, jml_soal)
  
  return render(request, 'pesertahsi/index.html', {'bank_soal': soal_acak})
