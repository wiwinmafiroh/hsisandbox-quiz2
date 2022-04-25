from django.shortcuts import render
from django.http import HttpResponse
from adminhsi.banksoal.banksoal import EvaluasiHarian

# Create your views here.
def adminhsi(request):
  bank_soal = EvaluasiHarian()
  jml_soal = len(EvaluasiHarian())
  return render(request, 'adminhsi/index.html', {'bank_soal': bank_soal, 'jml_soal': jml_soal})