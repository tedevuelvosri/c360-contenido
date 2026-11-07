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

# ---------------- POSTS (1080x1350) · SEMANA 7 (18-nov) ----------------
P = {}
P["w7a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Cierre fiscal · Cartera</div>
<h1 style="font-size:90px">Cuentas por cobrar viejas: <span class="hl">lo que la ley permite provisionar</span></h1>
<p class="lead">Antes del 31 de diciembre, revisa tu cartera con criterio tributario.</p>
{foot()}</div>"""
P["w7a_2"] = f"""<div class="s light" style="gap:34px;justify-content:center">
<div class="tag">La regla</div>
<h2><span class="hl">1% anual</span> sobre los créditos comerciales del ejercicio</h2>
<p class="lead">Los concedidos en el año y pendientes de cobro al cierre. La provisión acumulada no puede superar el 10% de la cartera total (art. 10, num. 11, LRTI).</p>
<div class="card"><div class="n">≠</div><div><h3>No aplica</h3><p>A créditos concedidos a socios, sus cónyuges o parientes, ni a sociedades relacionadas.</p></div></div>
{foot(light=True)}</div>"""
P["w7a_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Cuándo dar de baja</div>
<h2 style="margin-bottom:6px">Basta con <span class="hl">una</span> de estas condiciones</h2>
{card("01","Dos años registrado","Constar como incobrable en la contabilidad durante dos años o más.")}
{card("02","Tres años vencido","Más de tres años desde el vencimiento original del crédito.")}
{card("03","Acción prescrita","Que haya prescrito la acción para cobrarlo.")}
{card("04","Deudor insolvente","Quiebra o insolvencia del deudor, o sociedad deudora cancelada.")}
<p style="font-size:24px;color:#8A8D91">Reglamento a la LRTI, art. 28, num. 3.</p>
{foot(light=True)}</div>"""
P["w7a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">La cartera se revisa antes del cierre, <span class="hl">no en la declaración.</span></h2>
<p class="lead">Diagnóstico preventivo sin costo: reporte en 24 horas, solo con tu RUC y sin claves.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w7b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:44px">
<div class="tag">Prevención · Control SRI</div>
<h1 style="font-size:88px">Antes de una fiscalización: <span class="hl">4 preguntas</span> que tu contabilidad debe responder hoy</h1>
<p class="lead">Lo que está ordenado hoy se entrega en horas.</p>
{foot()}</div>"""
P["w7b_2"] = f"""<div class="s light" style="gap:38px;justify-content:center">
<div class="tag">Por qué</div>
<h2>Una revisión se responde con <span class="hl">documentos</span>, no con explicaciones</h2>
<p class="lead">Lo que no está ordenado se reconstruye después, con plazos cortos y bajo presión.</p>
<div class="card"><div class="n">✓</div><div><h3>El objetivo</h3><p>Que cada cifra declarada tenga su respaldo listo para mostrarse.</p></div></div>
{foot(light=True)}</div>"""
P["w7b_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Las 4 preguntas</div>
{card("01","¿Lo declarado cuadra?","IVA mensual, renta y estados financieros cuentan la misma historia.")}
{card("02","¿Cada gasto se sostiene?","Comprobante válido, relación con el negocio y pago bancarizado sobre USD 500.")}
{card("03","¿Las retenciones cuadran?","Las efectuadas, declaradas y pagadas; las recibidas, cruzadas con ingresos.")}
{card("04","¿Hay un expediente por período?","Comprobantes, conciliaciones y anexos ordenados y fáciles de encontrar.")}
{foot(light=True)}</div>"""
P["w7b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:78px">La mejor defensa se prepara <span class="hl">antes</span> del requerimiento.</h2>
<p class="lead">Revisamos tu situación con una mirada preventiva, sin pedirte claves.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1;white-space:nowrap;margin-left:20px">{date}</span></div>')
S["w7s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:28px;padding-bottom:360px">
<div class="tag">Calendario SRI · Esta semana</div>
<h2 style="font-size:70px">IVA y retenciones de octubre: <span class="hl">dígitos 6, 7 y 8</span></h2>
{due("6","vie 20 nov","Jornada suspendida (Decreto 507): declara antes")}
{due("7","lun 23 nov","El 22 cae domingo: pasa al lunes")}
{due("8","mar 24 nov")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. No dejes la declaración para el último día.</p>
{foot("")}</div>"""
S["w7s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:78px">¿Cuánto de tu cartera lleva <span class="hl">más de un año sin cobrarse?</span></h2>
<p class="lead">Antes del cierre, revisa qué se puede provisionar y qué ya debería darse de baja.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
S["w7s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Mito vs realidad</div>
<h2 style="font-size:66px"><span style="text-decoration:line-through;text-decoration-color:#5FE0E0;opacity:.75">“Si tengo la factura, el gasto es deducible aunque lo pague en efectivo.”</span></h2>
<div style="background:#FDFEFF;color:#0B1F6E;border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#2E8FD1;font-size:28px;letter-spacing:.12em;margin-bottom:14px">REALIDAD</p>
<p style="font-family:M;font-weight:800;font-size:42px;line-height:1.25">Sobre USD 500, el pago debe pasar por el sistema financiero para deducir el gasto y usar el crédito tributario de IVA.</p></div>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w7s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Prevención · Control SRI</div>
<h2 style="font-size:78px">Antes de una fiscalización: <span class="hl">4 preguntas que tu contabilidad debe responder hoy.</span></h2>
<p class="lead">Una revisión se responde con documentos, no con explicaciones.</p>
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
