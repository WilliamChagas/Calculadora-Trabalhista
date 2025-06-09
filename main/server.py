from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/formulario", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

@app.post("/resultado", response_class=HTMLResponse)
def resultado(
    request: Request,
    nome: str = Form(...),
    salario: float = Form(...),
    meses: int = Form(...),
    motivo: str = Form(...)
):
    # Vamos definir alguns valores padrão para os cálculos,
    # já que você não enviou os campos antes usados.
    
    # Exemplo: dias_trabalhados fixo, fgts_total calculado como 8% do salário * meses, aviso_previo dependendo do motivo
    dias_trabalhados = 0  # Sem dado no form, pode ajustar depois
    fgts_total = salario * meses * 0.08  # 8% do salário vezes meses trabalhados

    # Aviso prévio: só pago se demissão sem justa causa ou fim de contrato
    if motivo in ("demissao", "fim_contrato"):
        aviso_previo = salario
    else:
        aviso_previo = 0

    ferias = (salario / 12) * meses + (salario / 3)
    decimo_terceiro = (salario / 12) * meses
    multa_fgts = fgts_total * 0.4
    saldo_salario = (salario / 30) * dias_trabalhados  # dias_trabalhados = 0 por enquanto

    total = ferias + decimo_terceiro + aviso_previo + multa_fgts + saldo_salario

    return templates.TemplateResponse("resultado.html", {
        "request": request,
        "nome": nome,
        "salario": salario,
        "meses": meses,
        "motivo": motivo,
        "ferias": round(ferias, 2),
        "decimo_terceiro": round(decimo_terceiro, 2),
        "aviso_previo": round(aviso_previo, 2),
        "multa_fgts": round(multa_fgts, 2),
        "saldo_salario": round(saldo_salario, 2),
        "total": round(total, 2),
    })
