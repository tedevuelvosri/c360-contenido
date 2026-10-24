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

# ---------------- POSTS (1080x1350) · SEMANA 5 (04-nov) ----------------
P = {}
P["w5a_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<div class="tag">Prevención tributaria</div>
<h1 style="font-size:96px">¿Qué es una <span class="hl">glosa</span> del SRI?</h1>
<p class="lead">Y por qué se previene en el registro de cada día, no cuando llega el control.</p>
{foot()}</div>"""
P["w5a_2"] = f"""<div class="s light" style="gap:36px;justify-content:center">
<div class="tag">En simple</div>
<h2>Una diferencia que el SRI <span class="hl">determina</span> en tus declaraciones</h2>
<p class="lead">Surge tras un proceso de control: un ingreso que no declaraste, un gasto que considera no deducible o un crédito tributario sin sustento.</p>
<div class="card"><div class="n">=</div><div><h3>¿Qué implica?</h3><p>Impuesto adicional, intereses y posibles multas.</p></div></div>
{foot(light=True)}</div>"""
P["w5a_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">De dónde suelen salir</div>
<h2 style="margin-bottom:6px">Cuatro orígenes <span class="hl">frecuentes</span></h2>
{card("01","Gastos sin sustento","Sin comprobante válido o sin el medio de pago que exige la norma.")}
{card("02","Cifras que no cuadran","ATS, declaraciones y contabilidad con valores distintos.")}
{card("03","Retenciones mal aplicadas","No efectuadas, con porcentaje errado o sin declarar.")}
{card("04","Ingresos no declarados","Detectados por cruces de información del SRI.")}
{foot(light=True)}</div>"""
P["w5a_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">Una glosa se previene en el <span class="hl">día a día</span>, no en la respuesta al SRI.</h2>
<p class="lead">Diagnóstico preventivo sin costo: reporte en 24 horas, solo con tu RUC y sin claves.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""

P["w5b_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:44px">
<div class="tag">Visión regional · EC · PE · CO</div>
<h1 style="font-size:84px">¿Tu empresa opera en Ecuador, Perú o Colombia?</h1>
<p class="lead">La <b style="color:#5FE0E0">Decisión 578 de la CAN</b> evita que pagues dos veces impuesto por la misma renta.</p>
{foot()}</div>"""
P["w5b_2"] = f"""<div class="s light" style="gap:36px;justify-content:center">
<div class="tag">Qué es</div>
<h2>El régimen andino contra la <span class="hl">doble tributación</span></h2>
<p class="lead">Aplica entre los países miembros de la Comunidad Andina: Bolivia, Colombia, Ecuador y Perú.</p>
<div class="card"><div class="n">→</div><div><h3>Regla general</h3><p>La renta tributa solo en el país donde se genera. El otro país la considera exonerada.</p></div></div>
{foot(light=True)}</div>"""
P["w5b_3"] = f"""<div class="s light tight" style="gap:22px;justify-content:center">
<div class="tag">Reglas que conviene conocer</div>
<h2 style="margin-bottom:6px">¿Dónde <span class="hl">tributa</span> cada renta?</h2>
{card("01","Dividendos","En el país donde está domiciliada la empresa que los distribuye.")}
{card("02","Intereses","En el país donde se imputa y registra su pago.")}
{card("03","Servicios personales","Incluida la consultoría: donde se prestaron.")}
{card("04","Transporte","En el país donde está domiciliada la empresa.")}
{foot(light=True)}</div>"""
P["w5b_4"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:78px">Operar en la región es una oportunidad <span class="hl">si se planifica.</span></h2>
<p class="lead">Revisa cada operación y su sustento antes de facturar o pagar entre países.</p>
<div class="cta">{CTA}</div>
{foot("SÍGUENOS")}</div>"""

# ---------------- STORIES (1080x1920) ----------------
S = {}
def due(d,date,note=""):
    n = f'<p style="font-size:26px;color:#8A8D91;margin-top:6px">{note}</p>' if note else ""
    return (f'<div style="background:#FDFEFF;border-radius:26px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><span style="font-size:32px;color:#5a5f68">Dígito <b class="mono" style="color:#0B1F6E;font-size:56px">{d}</b></span>{n}</div>'
            f'<span class="mono" style="font-size:48px;color:#2E8FD1;white-space:nowrap;margin-left:20px">{date}</span></div>')
S["w5s1"] = f"""<div class="s navy glow" style="justify-content:center;gap:24px;padding-bottom:360px">
<div class="tag">Calendario SRI · Noviembre</div>
<h2 style="font-size:66px">IVA y retenciones de octubre: <span class="hl">dígitos 6 al 0</span></h2>
{due("6","vie 20 nov","Sin jornada (Decreto 507): declara antes")}
{due("7","lun 23 nov","El 22 cae domingo: pasa al lunes")}
{due("8","mar 24 nov")}
{due("9","jue 26 nov")}
{due("0","lun 30 nov","El 28 cae sábado: pasa al lunes")}
<p class="lead" style="font-size:30px">Noveno dígito del RUC. Declarar tarde genera multas e intereses.</p>
{foot("")}</div>"""
S["w5s2"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Pregunta para gerentes</div>
<h2 style="font-size:78px">¿Sabes qué gastos de tu empresa podría <span class="hl">objetar el SRI?</span></h2>
<p class="lead">Un gasto sin comprobante válido o sin el medio de pago que exige la norma puede terminar en una glosa.</p>
<div class="cta" style="background:#0B1F6E;color:#FDFEFF">Conversemos por mensaje directo</div>
{foot("", light=True)}</div>"""
S["w5s3"] = f"""<div class="s navy glow" style="justify-content:center;gap:40px">
<div class="tag">¿Sabías que?</div>
<h2 style="font-size:70px">Desde junio de 2026, tu declaración de IVA <span class="hl">solo vale si la pagas completa</span> al presentarla.</h2>
<div style="background:#FDFEFF;color:#0B1F6E;border-radius:26px;padding:36px 40px">
<p class="mono" style="color:#2E8FD1;font-size:28px;letter-spacing:.12em;margin-bottom:14px">QUÉ HACER</p>
<p style="font-family:M;font-weight:800;font-size:44px;line-height:1.25">Ten el saldo disponible en la cuenta antes de declarar.</p></div>
<p class="lead" style="font-size:28px">SRI · Resolución NAC-DGERCGC26-00000016</p>
<div class="cta">{CTA}</div>
{foot("")}</div>"""
S["w5s4"] = f"""<div class="s light" style="justify-content:center;gap:50px">
<div class="tag">Visión regional</div>
<h2 style="font-size:80px">¿Operas en Ecuador, Perú o Colombia? <span class="hl">No pagues dos veces.</span></h2>
<p class="lead">Qué es la Decisión 578 de la CAN y dónde tributa cada renta.</p>
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
