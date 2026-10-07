import asyncio, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).parent
A = (ROOT / "assets").as_uri()
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True); OUT2 = OUT

CSS = f"""
@font-face{{font-family:M;src:url({A}/montserrat-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:M;src:url({A}/montserrat-latin-800-normal.woff2);font-weight:800}}
@font-face{{font-family:M;src:url({A}/montserrat-latin-900-normal.woff2);font-weight:900}}
@font-face{{font-family:J;src:url({A}/jetbrains-mono-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:J;src:url({A}/jetbrains-mono-latin-700-normal.woff2);font-weight:700}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:var(--w);height:var(--h);font-family:Inter,sans-serif;overflow:hidden}}
.s{{position:relative;width:100%;height:100%;padding:var(--pad);display:flex;flex-direction:column}}
.navy{{background:linear-gradient(155deg,#071454 0%,#0B1F6E 60%,#132A8C 100%);color:#FDFEFF}}
.light{{background:#F6F8FB;color:#0B1F6E}}
.glow::after{{content:"";position:absolute;right:-180px;top:-180px;width:640px;height:640px;border-radius:50%;
 background:radial-gradient(circle,rgba(95,224,224,.28),transparent 70%)}}
.tag{{font-family:J;font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:#5FE0E0;
 border:2px solid rgba(95,224,224,.5);border-radius:40px;padding:10px 24px;align-self:flex-start}}
.light .tag{{color:#2E8FD1;border-color:#2E8FD1}}
h1{{font-family:M;font-weight:900;font-size:96px;line-height:1.04;letter-spacing:-.01em}}
h2{{font-family:M;font-weight:800;font-size:68px;line-height:1.1}}
p.lead{{font-size:38px;line-height:1.45;color:#C9D2E0}}
.light p.lead{{color:#3E4759}}
.hl{{color:#5FE0E0}} .light .hl{{color:#2E8FD1}}
.foot{{position:absolute;left:var(--pad);right:var(--pad);bottom:var(--fb);display:flex;align-items:center;justify-content:space-between;
 font-family:J;font-weight:500;font-size:26px;letter-spacing:.06em}}
.foot .b{{display:flex;align-items:center;gap:16px}}
.foot img{{height:46px}}
.navy .foot{{color:#C9D2E0}} .light .foot{{color:#8A8D91}}
.mono{{font-family:J;font-weight:700}}
.card{{background:#FDFEFF;border:2px solid #E1E7F5;border-radius:28px;padding:34px 38px;display:flex;gap:28px;align-items:flex-start}}
.card .n{{font-family:J;font-weight:700;font-size:34px;color:#0B1F6E;background:#E4FAFA;border-radius:16px;min-width:76px;height:76px;
 display:flex;align-items:center;justify-content:center}}
.card h3{{font-family:M;font-weight:800;font-size:42px;line-height:1.2;color:#0B1F6E;margin-bottom:8px}}
.card p{{font-size:32px;line-height:1.4;color:#5a5f68}}
.tight .card{{padding:24px 34px}} .tight .card p{{font-size:30px}}
.cta{{background:#5FE0E0;color:#071454;font-family:M;font-weight:800;font-size:40px;border-radius:60px;padding:30px 46px;align-self:flex-start}}
"""

def foot(right="DESLIZA →", light=False):
    sym = "sym_color.png" if light else "sym_white.png"
    return f'<div class="foot"><div class="b"><img src="{A}/{sym}">@contabilidad360ec</div><div>{right}</div></div>'

def card(n,t,d,extra=""): return f'<div class="card" {extra}><div class="n">{n}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
CTA = "Envíanos tu RUC por mensaje directo"

# ---------------- POSTS (1080x1350) · SEMANA 2 ----------------
P = {}
P["w2a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Contabilidad bajo NIIF</div>
<h1 style="font-size:92px">¿Tus estados financieros te <span class="hl">abren puertas</span> o te las cierran?</h1>
<p class="lead">Bancos, socios e inversionistas deciden con base en tus números.</p>
{foot()}</div>"""
P["w2a_2"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Antes de un crédito</div>
<h2 style="margin-bottom:6px">Lo que un banco <span class="hl">mira primero</span></h2>
{card("01","Estados financieros consistentes","Que lo que muestras al banco coincida con lo declarado al SRI.")}
{card("02","Flujo de caja que respalde el pago","No basta con vender: hay que demostrar liquidez.")}
{card("03","Cumplimiento al día","Balances presentados a la Supercías y sin obligaciones pendientes.")}
{foot(light=True)}</div>"""
def col(title,items,hi=False):
    bg = "background:#0B1F6E;color:#FDFEFF;border-color:#0B1F6E" if hi else ""
    li = "".join(f'<p style="font-size:30px;line-height:1.35;padding:16px 0;border-top:2px solid {"rgba(255,255,255,.15)" if hi else "#E1E7F5"};{"color:#C9D2E0" if hi else ""}">{i}</p>' for i in items)
    return f'<div class="card" style="flex:1;flex-direction:column;gap:6px;{bg}"><h3 style="{"color:#5FE0E0" if hi else ""};margin-bottom:12px">{title}</h3>{li}</div>'
P["w2a_3"] = f"""<div class="s light" style="gap:34px;justify-content:center">
<div class="tag">La diferencia</div>
<h2>Contabilidad para declarar vs. <span class="hl">para decidir</span></h2>
<div style="display:flex;gap:24px">
{col("Para declarar",["Registra lo que ya pasó","Se arma a fin de mes","Su meta es cumplir con el SRI"])}
{col("Para decidir",["Conciliada y bajo NIIF","Reportes mensuales para gerencia","Flujo de caja proyectado"],True)}
</div>
{foot(light=True)}</div>"""
P["w2a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:84px">Números claros para <span class="hl">decidir con confianza.</span></h2>
<p class="lead">Empieza por un diagnóstico preventivo sin costo: reporte en 24 horas, solo con tu RUC.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w2b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Dirección financiera</div>
<h1 style="font-size:96px">¿Necesitas un contador o un <span class="hl">CFO externo?</span></h1>
<p class="lead">La diferencia está en mirar hacia atrás o hacia adelante.</p>
{foot()}</div>"""
P["w2b_2"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Contabilidad tradicional</div>
<h2 style="margin-bottom:6px">Cumple. <span class="hl">Y es necesaria.</span></h2>
{card("01","Registra facturas y movimientos","Mantiene los libros al día.")}
{card("02","Declara a tiempo","IVA, retenciones, ATS y renta.")}
{card("03","Reacciona","Atiende las notificaciones cuando llegan.")}
{foot(light=True)}</div>"""
P["w2b_3"] = f"""<div class="s light" style="gap:26px;justify-content:center">
<div class="tag">CFO externo</div>
<h2 style="margin-bottom:6px">Además, <span class="hl">dirige.</span></h2>
{card("01","Analiza rentabilidad y flujo de caja","Sabes qué línea de negocio deja dinero.")}
{card("02","Planifica impuestos de forma legal","Ahorro tributario dentro de la norma.")}
{card("03","Anticipa contingencias","Corrige antes de que llegue la notificación.")}
{card("04","Se sienta con gerencia","Reunión mensual de resultados.")}
{foot(light=True)}</div>"""
P["w2b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:84px">En Contabilidad360 hacemos <span class="hl">las dos cosas.</span></h2>
<p class="lead">Cumplimiento impecable y visión de dirección financiera, con atención directa de la socia fundadora.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1">{date}</span></div>')
S["w2s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Calendario SRI · Esta semana</div>
<h2 style="font-size:76px">Vencen <span class="hl">IVA y retenciones</span> para estos dígitos</h2>
{due("4","vie 16 oct")}
{due("5","lun 19 oct","El 18 cae domingo: pasa al lunes")}
{due("6","mar 20 oct")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. Declarar tarde genera multas e intereses.</p>
{foot("")}</div>"""
S["w2s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:84px">¿Sabes hoy cuánto <span class="hl">flujo de caja</span> tendrás en 3 meses?</h2>
<p class="lead">Si la respuesta es no, tus números te están diciendo menos de lo que podrían.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
mini = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.08);border-radius:20px;padding:26px 32px">'
               f'<span style="font-size:34px">{t}</span><span class="mono" style="color:#5FE0E0;font-size:30px">✓</span></div>'
               for t in ["Declaraciones IVA y Renta","Cumplimiento Supercías","Anexo Transaccional (ATS)","Nómina y aportes IESS"])
S["w2s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Diagnóstico preventivo</div>
<h2 style="font-size:80px">Tu reporte en <span class="hl">24 horas</span> revisa:</h2>
<div style="display:flex;flex-direction:column;gap:16px">{mini}</div>
<p class="lead">Solo con tu RUC. Sin claves. Sin costo.</p>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w2s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Dirección financiera</div>
<h2 style="font-size:86px">¿Contador o <span class="hl">CFO externo?</span></h2>
<p class="lead">Te explicamos la diferencia, y por qué tu empresa podría necesitar las dos cosas.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Míralo en el perfil</div>
{foot("", light=True)}</div>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h, pad, fb in [(k,v,1080,1350,"80px","60px") for k,v in P.items()] + [(k,v,1080,1920,"80px","300px") for k,v in S.items()]:
            pg = await b.new_page(viewport={"width":w,"height":h})
            hp = OUT2/f"{name}.html"
            hp.write_text(f"<html><head><meta charset=utf-8><style>:root{{--w:{w}px;--h:{h}px;--pad:{pad};--fb:{fb}}}{CSS}</style></head><body>{html}</body></html>")
            await pg.goto(hp.as_uri()); await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(OUT2/f"{name}.jpg"), type="jpeg", quality=92)
            await pg.close()
        await b.close()
asyncio.run(main())
