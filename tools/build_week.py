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

# ---------------- POSTS (1080x1350) · SEMANA 9 (2-dic) ----------------
P = {}
P["w9a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Cierre contable 2026</div>
<h1 style="font-size:86px">Revisa tus comprobantes electrónicos <span class="hl">antes del 31 de diciembre</span></h1>
<p class="lead">Cuatro controles que conviene hacer ahora, no en abril.</p>
{foot()}</div>"""
P["w9a_2"] = f"""<div class="s light" style="gap:38px;justify-content:center">
<div class="tag">Por qué ahora</div>
<h2>Lo que no se corrige en el cierre <span class="hl">llega a tu declaración de renta</span></h2>
<p class="lead">Y también a tus estados financieros. Un comprobante mal registrado en diciembre se convierte en una diferencia difícil de explicar después.</p>
<div class="card"><div class="n">✓</div><div><h3>La regla</h3><p>Cada gasto con su comprobante válido. Cada comprobante, en tu contabilidad.</p></div></div>
{foot(light=True)}</div>"""
P["w9a_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Los 4 controles</div>
{card("01","Recibidos vs registros","Cruza los comprobantes recibidos en el portal del SRI con tu contabilidad: lo que falta y lo que sobra.")}
{card("02","Retenciones","Las que emitiste y las que te hicieron deben cuadrar con tus declaraciones.")}
{card("03","Datos del proveedor","RUC, razón social y sustento del gasto. Lo mal documentado no se defiende.")}
{card("04","Transporte en 2027","Desde el 1 de enero, el gasto de transporte comercial se sustenta con factura de la operadora, no del socio.")}
{foot(light=True)}</div>"""
P["w9a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:78px">Un cierre ordenado <span class="hl">es la mejor defensa de tus gastos.</span></h2>
<p class="lead">Revisamos cómo se reflejan tus comprobantes en tus declaraciones, sin pedirte claves.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:24px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:52px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:46px;color:#2E8FD1;white-space:nowrap;margin-left:20px">{date}</span></div>')
S["w9s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:22px;padding-bottom:360px">
<div class="tag">Calendario SRI · Diciembre</div>
<h2 style="font-size:64px">IVA y retenciones de noviembre: <span class="hl">dígitos 1 al 5</span></h2>
{due("1","jue 10 dic")}
{due("2","lun 14 dic","El 12 cae sábado: pasa al lunes")}
{due("3","lun 14 dic")}
{due("4","mié 16 dic")}
{due("5","vie 18 dic")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. Dígitos 6 al 0: 21, 22, 24 y 28 de diciembre.</p>
{foot("")}</div>"""
S["w9s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:76px">¿Los comprobantes que recibes en el SRI <span class="hl">cuadran con tu contabilidad?</span></h2>
<p class="lead">El lunes: 4 controles de comprobantes electrónicos antes del cierre 2026.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Míralo el lunes en el perfil</div>
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
