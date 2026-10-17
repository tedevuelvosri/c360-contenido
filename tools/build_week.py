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

# ---------------- POSTS (1080x1350) · SEMANA 4 (28-oct) ----------------
P = {}
P["w4a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Prevención tributaria</div>
<h1 style="font-size:92px">Llegó una notificación del SRI. <span class="hl">¿Y ahora?</span></h1>
<p class="lead">Cómo respondas define cuánto te cuesta. Esto es lo que conviene hacer, y lo que no.</p>
{foot()}</div>"""
P["w4a_2"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Antes de responder</div>
<h2 style="margin-bottom:6px">Tres pasos <span class="hl">con calma</span></h2>
{card("01","Lee qué piden y el plazo","Exactamente qué información y hasta cuándo.")}
{card("02","Reúne el sustento","Comprobantes, contratos, conciliaciones y registros.")}
{card("03","Cruza las cifras","Declaraciones, ATS y contabilidad deben contar la misma historia.")}
{foot(light=True)}</div>"""
P["w4a_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Errores que encarecen</div>
<h2 style="margin-bottom:6px">Lo que <span class="hl">no</span> debes hacer</h2>
{card("01","Responder fuera de plazo","El tiempo corre desde la notificación.")}
{card("02","Entregar información incompleta","Datos sueltos o contradictorios abren más preguntas.")}
{card("03","Ignorar la notificación","No desaparece: el proceso sigue sin tu versión.")}
{card("04","Corregir sin entender el origen","Sin saber de dónde viene la diferencia, se repite.")}
{foot(light=True)}</div>"""
P["w4a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">La mejor respuesta al SRI se prepara <span class="hl">antes de que llegue.</span></h2>
<p class="lead">Diagnóstico preventivo sin costo: reporte en 24 horas, solo con tu RUC y sin claves.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w4b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Flujo de caja</div>
<h1 style="font-size:96px">¿Sabes cuánta caja tendrás en <span class="hl">90 días?</span></h1>
<p class="lead">Un flujo de caja proyectado te avisa antes de que falte dinero, no después.</p>
{foot()}</div>"""
P["w4b_2"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Cómo armarlo</div>
<h2 style="margin-bottom:6px">Tres bases <span class="hl">realistas</span></h2>
{card("01","Parte del saldo real","El saldo bancario conciliado, no el estimado.")}
{card("02","Proyecta cobros reales","Con tus días de cobro reales, no con lo facturado.")}
{card("03","Proyecta todos los pagos","Proveedores, nómina, impuestos y obligaciones financieras.")}
{foot(light=True)}</div>"""
P["w4b_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Pagos que se olvidan</div>
<h2 style="margin-bottom:6px">Los que <span class="hl">desordenan la caja</span></h2>
{card("01","Décimo tercer sueldo","Se paga hasta el 24 de diciembre.")}
{card("02","Impuesto a la Renta anual","El resultado del año también sale de caja.")}
{card("03","Cuotas de préstamos","Capital e intereses, mes a mes.")}
{card("04","IVA y retenciones","Vencimientos mensuales según tu RUC.")}
{foot(light=True)}</div>"""
P["w4b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">Proyectar no es adivinar: <span class="hl">es decidir con anticipación.</span></h2>
<p class="lead">Actualízalo cada mes con tu contabilidad cerrada y conciliada.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1">{date}</span></div>')
S["w4s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:24px;padding-bottom:360px">
<div class="tag">Calendario SRI · Noviembre</div>
<h2 style="font-size:66px">Vencen <span class="hl">IVA y retenciones</span> de octubre</h2>
{due("1","mar 10 nov")}
{due("2","jue 12 nov")}
{due("3","lun 16 nov","El 14 cae sábado: pasa al lunes")}
{due("4","lun 16 nov")}
{due("5","mié 18 nov")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. Declarar tarde genera multas e intereses.</p>
{foot("")}</div>"""
S["w4s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:78px">¿Ya tienes provisionado el <span class="hl">décimo tercer sueldo</span> de tu equipo?</h2>
<p class="lead">Se paga hasta el 24 de diciembre y se calcula con lo percibido del 1 de diciembre de 2025 al 30 de noviembre de 2026.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
S["w4s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Mito vs. realidad</div>
<div style="background:rgba(255,255,255,.08);border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#8A8D91;font-size:28px;letter-spacing:.12em;margin-bottom:14px">MITO</p>
<p style="font-family:M;font-weight:800;font-size:52px;line-height:1.2">“La contabilidad solo sirve para pagar impuestos.”</p></div>
<div style="background:#FDFEFF;color:#0B1F6E;border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#2E8FD1;font-size:28px;letter-spacing:.12em;margin-bottom:14px">REALIDAD</p>
<p style="font-family:M;font-weight:800;font-size:46px;line-height:1.25">Bien llevada, es la base para decidir: rentabilidad, flujo de caja y acceso a crédito.</p></div>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w4s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Flujo de caja</div>
<h2 style="font-size:86px">¿Sabes cuánta caja tendrás en <span class="hl">90 días?</span></h2>
<p class="lead">Cómo armar un flujo de caja proyectado y qué pagos no olvidar.</p>
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
