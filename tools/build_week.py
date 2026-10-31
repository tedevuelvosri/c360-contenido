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

# ---------------- POSTS (1080x1350) · SEMANA 6 (11-nov) ----------------
P = {}
P["w6a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Nómina · Provisiones</div>
<h1 style="font-size:92px">Décimo cuarto sueldo: <span class="hl">dos regiones, dos calendarios</span></h1>
<p class="lead">Lo que cambia entre Costa y Sierra, y por qué conviene provisionarlo cada mes.</p>
{foot()}</div>"""
P["w6a_2"] = f"""<div class="s light" style="gap:36px;justify-content:center">
<div class="tag">Qué es</div>
<h2>Una bonificación anual equivalente a <span class="hl">un salario básico unificado</span></h2>
<p class="lead">En 2026 el salario básico unificado es de USD 482. Si el trabajador no completó el período, se paga la parte proporcional.</p>
<div class="card"><div class="n">÷</div><div><h3>Proporcional</h3><p>Salario básico ÷ 12 × meses trabajados en el período.</p></div></div>
{foot(light=True)}</div>"""
P["w6a_3"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Dos calendarios</div>
<h2 style="margin-bottom:6px">Período y <span class="hl">fecha de pago</span></h2>
{card("01","Costa y Galápagos","Período del 1 de marzo al último día de febrero. Se paga hasta el 15 de marzo.")}
{card("02","Sierra y Amazonía","Período del 1 de agosto al 31 de julio. Se paga hasta el 15 de agosto.")}
{card("→","Hoy","Si tienes personal en la Costa, ya corren meses del período que se paga en marzo.")}
{foot(light=True)}</div>"""
P["w6a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">Lo que se provisiona cada mes <span class="hl">no sorprende</span> en el mes de pago.</h2>
<p class="lead">Diagnóstico preventivo sin costo: reporte en 24 horas, solo con tu RUC y sin claves.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w6b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:44px">
<div class="tag">Sustento tributario</div>
<h1 style="font-size:96px"><span class="hl">Siete años:</span> lo que tu empresa debe conservar</h1>
<p class="lead">El plazo que fija el SRI para guardar tus comprobantes, y por qué es tu mejor defensa.</p>
{foot()}</div>"""
P["w6b_2"] = f"""<div class="s light" style="gap:36px;justify-content:center">
<div class="tag">La norma</div>
<h2>Los comprobantes se conservan <span class="hl">durante siete años</span></h2>
<p class="lead">Lo establece el artículo 41 del Reglamento de Comprobantes de Venta, Retención y Documentos Complementarios.</p>
<div class="card"><div class="n">@</div><div><h3>¿Y los electrónicos?</h3><p>Quien emite por medios electrónicos debe mantener el archivo digital de cada comprobante.</p></div></div>
{foot(light=True)}</div>"""
P["w6b_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Qué incluye</div>
<h2 style="margin-bottom:6px">Documentos que <span class="hl">debes guardar</span></h2>
{card("01","Facturas","Las que emites y las que recibes.")}
{card("02","Liquidaciones de compra","De bienes y de prestación de servicios.")}
{card("03","Notas de crédito y débito","Cada ajuste a una venta o compra.")}
{card("04","Retenciones y guías de remisión","Comprobantes de retención y traslados de mercadería.")}
{foot(light=True)}</div>"""
P["w6b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:78px">Un gasto sin sustento <span class="hl">no se defiende</span> ante un control.</h2>
<p class="lead">Ordena y respalda cada comprobante hoy, no cuando el SRI lo pida.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1;white-space:nowrap;margin-left:20px">{date}</span></div>')
S["w6s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:28px;padding-bottom:360px">
<div class="tag">Calendario SRI · Esta semana</div>
<h2 style="font-size:70px">IVA y retenciones de octubre: <span class="hl">dígitos 2, 3 y 4</span></h2>
{due("2","jue 12 nov")}
{due("3","lun 16 nov","El 14 cae sábado: pasa al lunes")}
{due("4","lun 16 nov")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. Aunque no hayas tenido ventas, la declaración se presenta.</p>
{foot("")}</div>"""
S["w6s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:78px">Si hoy te pidieran una factura de compra de hace cinco años, <span class="hl">¿la encontrarías?</span></h2>
<p class="lead">Los comprobantes se conservan durante siete años. Sin ellos, el gasto pierde su sustento.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
S["w6s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Mito vs realidad</div>
<h2 style="font-size:70px"><span style="text-decoration:line-through;text-decoration-color:#5FE0E0;opacity:.75">“El décimo cuarto se paga igual en todo el país.”</span></h2>
<div style="background:#FDFEFF;color:#0B1F6E;border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#2E8FD1;font-size:28px;letter-spacing:.12em;margin-bottom:14px">REALIDAD</p>
<p style="font-family:M;font-weight:800;font-size:44px;line-height:1.25">Costa y Galápagos pagan hasta el 15 de marzo. Sierra y Amazonía, hasta el 15 de agosto.</p></div>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w6s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Sustento tributario</div>
<h2 style="font-size:80px">Siete años: <span class="hl">lo que tu empresa debe conservar.</span></h2>
<p class="lead">Qué comprobantes guardar y por qué son tu mejor defensa ante un control.</p>
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
