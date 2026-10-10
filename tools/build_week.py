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

# ---------------- POSTS (1080x1350) · SEMANA 3 ----------------
P = {}
P["w3a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Control contable</div>
<h1 style="font-size:96px">¿Tu contabilidad cuadra con tu <span class="hl">banco?</span></h1>
<p class="lead">La conciliación bancaria es el primer control de unos estados financieros confiables.</p>
{foot()}</div>"""
P["w3a_2"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Qué es conciliar</div>
<h2 style="margin-bottom:6px">Comparar, explicar y <span class="hl">corregir</span></h2>
{card("01","Libros vs. estado de cuenta","Cada mes, al cierre, se comparan ambos saldos.")}
{card("02","Explicar cada diferencia","Cheques en tránsito, depósitos no registrados, comisiones.")}
{card("03","Corregir y documentar","Cada partida pendiente, con su sustento.")}
{foot(light=True)}</div>"""
P["w3a_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Señales de alerta</div>
<h2 style="margin-bottom:6px">Si ves esto, <span class="hl">algo no cuadra</span></h2>
{card("01","Partidas pendientes de hace meses","Diferencias que nadie explicó y siguen ahí.")}
{card("02","Depósitos sin identificar","Ingresos que no sabes de dónde vienen.")}
{card("03","Comisiones sin registrar","Gastos bancarios que no aparecen en tus libros.")}
{card("04","Conciliación “cuando hay tiempo”","Si no es mensual, los errores se acumulan.")}
{foot(light=True)}</div>"""
P["w3a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">Sin conciliación, tu flujo de caja es <span class="hl">una suposición.</span></h2>
<p class="lead">Empieza por un diagnóstico preventivo sin costo: reporte en 24 horas, solo con tu RUC.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w3b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Gestión financiera</div>
<h1 style="font-size:96px">5 indicadores que deberías ver <span class="hl">cada mes</span></h1>
<p class="lead">Sin ellos, las decisiones se toman con intuición y no con números.</p>
{foot()}</div>"""
P["w3b_2"] = f"""<div class="s light" style="gap:30px;justify-content:center">
<div class="tag">Rentabilidad</div>
<h2 style="margin-bottom:6px">¿Tu negocio <span class="hl">gana dinero?</span></h2>
{card("01","Margen bruto","Cuánto queda de cada venta después del costo directo.")}
{card("02","Margen neto","Lo que realmente queda después de gastos e impuestos.")}
{foot(light=True)}</div>"""
P["w3b_3"] = f"""<div class="s light" style="gap:26px;justify-content:center">
<div class="tag">Liquidez</div>
<h2 style="margin-bottom:6px">¿Tienes <span class="hl">caja para operar?</span></h2>
{card("03","Liquidez corriente","Activo corriente ÷ pasivo corriente.")}
{card("04","Días de cobro","Cuánto tardan tus clientes en pagarte.")}
{card("05","Días de pago","Cuánto tardas tú en pagar a tus proveedores.")}
{foot(light=True)}</div>"""
P["w3b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">Indicadores confiables necesitan <span class="hl">contabilidad confiable.</span></h2>
<p class="lead">Conciliada, bajo NIIF y con reportes mensuales para gerencia.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1">{date}</span></div>')
S["w3s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:24px;padding-bottom:360px">
<div class="tag">Calendario SRI · Próximos días</div>
<h2 style="font-size:68px">Vencen <span class="hl">IVA y retenciones</span> para estos dígitos</h2>
{due("7","jue 22 oct","Hoy")}
{due("8","lun 26 oct","El 24 cae sábado: pasa al lunes")}
{due("9","lun 26 oct")}
{due("0","mié 28 oct")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. Declarar tarde genera multas e intereses.</p>
{foot("")}</div>"""
S["w3s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:80px">Si el año cerrara hoy, ¿sabrías cuánto pagarías de <span class="hl">Impuesto a la Renta?</span></h2>
<p class="lead">El ejercicio fiscal cierra el 31 de diciembre. Todavía hay tiempo para planificar, dentro de la norma.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
S["w3s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">Mito vs. realidad</div>
<div style="background:rgba(255,255,255,.08);border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#8A8D91;font-size:28px;letter-spacing:.12em;margin-bottom:14px">MITO</p>
<p style="font-family:M;font-weight:800;font-size:52px;line-height:1.2">“Si el SRI no me ha notificado, todo está bien.”</p></div>
<div style="background:#FDFEFF;color:#0B1F6E;border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#2E8FD1;font-size:28px;letter-spacing:.12em;margin-bottom:14px">REALIDAD</p>
<p style="font-family:M;font-weight:800;font-size:46px;line-height:1.25">Las diferencias se acumulan en silencio. Revisar antes cuesta menos que corregir después.</p></div>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w3s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Gestión financiera</div>
<h2 style="font-size:86px">5 indicadores que deberías ver <span class="hl">cada mes</span></h2>
<p class="lead">Rentabilidad y liquidez, explicadas sin jerga.</p>
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
