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


def item(when, what):
    return (f'<div class="card" style="padding:22px 30px;gap:22px;align-items:center">'
            f'<div class="mono" style="min-width:215px;white-space:nowrap;font-size:23px;color:#2E8FD1;letter-spacing:.04em">{when}</div>'
            f'<p style="font-size:29px;line-height:1.35;color:#3E4759">{what}</p></div>')
P = {}
P["ck_1"] = f"""<div class="s navy glow" style="justify-content:center;gap:46px">
<div class="tag">Checklist empresarial</div>
<h1 style="font-size:96px">Noviembre a febrero: <span class="hl">el calendario</span> que tu empresa no puede pasar por alto</h1>
<p class="lead">Cierre de año, décimos, anexos y reportes. Guárdalo y revisa mes a mes.</p>
{foot()}</div>"""
P["ck_2"] = f"""<div class="s light" style="gap:18px;justify-content:center">
<div class="tag">Noviembre y diciembre</div>
<h2 style="font-size:60px;margin-bottom:8px">Cierra el año <span class="hl">sin novedades</span></h2>
{item("CADA MES","IVA, retenciones y ATS según el noveno dígito del RUC, y planillas del IESS.")}
{item("NOVIEMBRE","Matriculación vehicular: en Quito corresponde a placas terminadas en 0.")}
{item("24 DIC","Pago del décimo tercer sueldo a quienes lo acumulan.")}
{item("31 DIC","Cierre contable: revisa comprobantes electrónicos y concilia antes de fin de año.")}
{foot(light=True)}</div>"""
P["ck_3"] = f"""<div class="s light" style="gap:18px;justify-content:center">
<div class="tag">Enero</div>
<h2 style="font-size:60px;margin-bottom:8px">Arranca el año <span class="hl">al día</span></h2>
{item("10 AL 28","IVA semestral del segundo semestre, para quienes declaran semestralmente, según el noveno dígito.")}
{item("DÍGITOS 1-5","Registro del pago del décimo tercero en el Ministerio del Trabajo, según su cronograma.")}
{item("DESDE EL 21","Anexo RDEP de retenciones en relación de dependencia, según el noveno dígito.")}
{item("PREDIAL","En Quito hay descuento por pronto pago desde el 1 de enero (en 2026 fue del 10% hasta el 15).")}
{foot(light=True)}</div>"""
P["ck_4"] = f"""<div class="s light" style="gap:18px;justify-content:center">
<div class="tag">Febrero</div>
<h2 style="font-size:60px;margin-bottom:8px">Anexos y <span class="hl">reportes anuales</span></h2>
{item("HASTA EL 7","Cierra el plazo del Anexo RDEP, según el noveno dígito del RUC.")}
{item("DÍGITOS 6-0","Registro del pago del décimo tercero en el Ministerio del Trabajo.")}
{item("10 AL 28","REBEFICS: reporte de beneficiarios finales y composición societaria, según el noveno dígito.")}
{item("10 AL 28","Anexo de gastos personales, para personas naturales que usan la rebaja.")}
{foot(light=True)}</div>"""
P["ck_5"] = f"""<div class="s navy glow" style="justify-content:center;gap:48px">
<h2 style="font-size:80px">No dejes los anexos <span class="hl">para el último día.</span></h2>
<p class="lead">Los sistemas suelen saturarse en las fechas límite. Si prefieres enfocarte en tu negocio, nosotros llevamos el calendario por ti.</p>
<div class="cta">{CTA}</div>
{foot("GUARDA ESTE POST")}</div>"""
S = {}
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
