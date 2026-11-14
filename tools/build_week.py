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

# ---------------- POSTS (1080x1350) · SEMANA 8 (25-nov) ----------------
P = {}
P["w8a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Facturación electrónica</div>
<h1 style="font-size:88px">Anular una factura electrónica: <span class="hl">plazos y reglas vigentes</span></h1>
<p class="lead">Un error de facturación también es un error contable. Corregirlo tiene fecha límite.</p>
{foot()}</div>"""
P["w8a_2"] = f"""<div class="s light" style="gap:34px;justify-content:center">
<div class="tag">El plazo</div>
<h2>En línea, hasta el <span class="hl">día 7 del mes siguiente</span> a la emisión</h2>
<p class="lead">Así lo fija la Resolución NAC-DGERCGC25-00000017 del SRI. Antes el plazo llegaba al día 10.</p>
<div class="card"><div class="n">→</div><div><h3>Pasado el plazo</h3><p>La factura solo se anula con nota de crédito, y únicamente en los casos que prevé el Reglamento de Comprobantes de Venta.</p></div></div>
{foot(light=True)}</div>"""
P["w8a_3"] = f"""<div class="s light tight" style="gap:24px;justify-content:center">
<div class="tag">Lo que cambió</div>
<h2 style="margin-bottom:6px">Tres reglas que <span class="hl">conviene tener presentes</span></h2>
{card("01","Consumidor final","Desde el 1 de enero de 2026, estas facturas no se anulan ni admiten nota de crédito.")}
{card("02","Aceptación del receptor","Anular notas de crédito, notas de débito y retenciones requiere que el receptor acepte.")}
{card("03","Cinco días hábiles","Si el receptor no responde en ese plazo, la solicitud queda sin efecto y el comprobante sigue válido.")}
{foot(light=True)}</div>"""
P["w8a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:78px">Facturar bien a la primera <span class="hl">cuesta menos que corregir.</span></h2>
<p class="lead">Revisamos cómo se reflejan tus comprobantes en tus declaraciones, sin pedirte claves.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w8b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:44px">
<div class="tag">Dirección financiera</div>
<h1 style="font-size:90px">Presupuesto 2027: <span class="hl">4 decisiones</span> antes de enero</h1>
<p class="lead">Un presupuesto no es una hoja de cálculo. Es el plan con el que tu empresa decide.</p>
{foot()}</div>"""
P["w8b_2"] = f"""<div class="s light" style="gap:38px;justify-content:center">
<div class="tag">Punto de partida</div>
<h2>Se construye sobre <span class="hl">cifras reales</span>, no sobre deseos</h2>
<p class="lead">Ventas, márgenes y gastos de 2026, conciliados y cerrados. Si la base está mal, todo lo que se proyecte encima también.</p>
<div class="card"><div class="n">✓</div><div><h3>Primero, el cierre</h3><p>Un año bien cerrado es el mejor insumo para planificar el siguiente.</p></div></div>
{foot(light=True)}</div>"""
P["w8b_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Las 4 decisiones</div>
{card("01","Metas de venta por línea","Por producto, servicio o cliente, con supuestos escritos y medibles.")}
{card("02","Estructura de costos","Qué es fijo, qué es variable y qué margen mínimo vas a defender.")}
{card("03","Flujo de caja mes a mes","Incluye impuestos, décimos e inversiones, no solo ventas y gastos.")}
{card("04","Revisión mensual","Real contra presupuesto, cada mes, con ajustes a tiempo.")}
{foot(light=True)}</div>"""
P["w8b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:78px">Planificar en diciembre <span class="hl">evita improvisar en marzo.</span></h2>
<p class="lead">Dirección contable y tributaria estratégica para tu empresa.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1;white-space:nowrap;margin-left:20px">{date}</span></div>')
S["w8s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:28px;padding-bottom:360px">
<div class="tag">Calendario SRI · Esta semana</div>
<h2 style="font-size:70px">IVA y retenciones de octubre: <span class="hl">dígitos 9 y 0</span></h2>
{due("9","jue 26 nov")}
{due("0","lun 30 nov","El 28 cae sábado: pasa al lunes")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. En diciembre arranca otra vez el dígito 1: jueves 10.</p>
{foot("")}</div>"""
S["w8s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:78px">¿Cuándo fue la última vez que <span class="hl">contaste tu inventario?</span></h2>
<p class="lead">Si la cifra del balance no coincide con lo que hay en bodega, las decisiones se toman sobre un número equivocado.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
S["w8s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Mito vs realidad</div>
<h2 style="font-size:66px"><span style="text-decoration:line-through;text-decoration-color:#5FE0E0;opacity:.75">“Una factura electrónica se puede anular cuando sea.”</span></h2>
<div style="background:#FDFEFF;color:#0B1F6E;border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#2E8FD1;font-size:28px;letter-spacing:.12em;margin-bottom:14px">REALIDAD</p>
<p style="font-family:M;font-weight:800;font-size:42px;line-height:1.25">En línea, solo hasta el día 7 del mes siguiente. Después, únicamente con nota de crédito. Y a consumidor final ya no se anula.</p></div>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w8s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Dirección financiera</div>
<h2 style="font-size:78px">Presupuesto 2027: <span class="hl">4 decisiones antes de enero.</span></h2>
<p class="lead">Planificar en diciembre evita improvisar en marzo.</p>
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
