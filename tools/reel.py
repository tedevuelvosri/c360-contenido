import asyncio, pathlib, subprocess, sys
from playwright.async_api import async_playwright
sys.path.insert(0,'.')
ROOT=pathlib.Path(__file__).parent; A=(ROOT/"assets").as_uri()
src=open(ROOT/"build_week.py").read(); CSS=src[src.index('CSS = f"""')+10:src.index('"""',src.index('CSS = f"""')+10)]
CSS=CSS.replace("{{","{").replace("}}","}").replace("{A}",A)
FPS=30; DUR=24
# scenes: (start,end,html)
def sc(a,b,html): return f'<div class="scene" style="--a:{a}s;--d:{b-a}s">{html}</div>'
SC = [
 sc(0,4.2,'<div class="tag">Facturación · Transporte 2027</div><h1 style="font-size:84px">¿Contratas transporte de carga o de personal? <span class="hl">Tus facturas cambian en enero</span></h1>'),
 sc(4.2,8.4,'<div class="num">01</div><h2 style="font-size:74px">Hasta el 31 de diciembre de 2026, <span class="hl">el socio aún puede facturarte</span></h2><p class="lead">Es el régimen transitorio de la Resolución NAC-DGERCGC26-00000028 del SRI.</p>'),
 sc(8.4,12.6,'<div class="num">02</div><h2 style="font-size:74px">Desde el 1 de enero de 2027, <span class="hl">te factura la operadora</span></h2><p class="lead">El socio factura solo a su operadora. La factura al cliente incluye la placa del vehículo.</p>'),
 sc(12.6,16.6,'<div class="num">03</div><h2 style="font-size:66px">Carga pesada y liviana, escolar e institucional, turístico, <span class="hl">mixto y alternativo-excepcional</span></h2><p class="lead">No aplica a taxis.</p>'),
 sc(16.6,19.8,'<h2 style="font-size:76px">El gasto se sustenta <span class="hl">con factura de la operadora.</span></h2><p class="lead">Revisa a tus proveedores de transporte antes de enero (Res. NAC-DGERCGC26-00000024).</p>'),
 sc(19.8,24,f'<img src="{A}/sym_white.png" style="width:200px"><div class="tag">Diagnóstico preventivo</div><h2 style="font-size:80px">Revisamos tus obligaciones en <span class="hl">24 horas.</span></h2><p class="lead">Solo con tu RUC. Sin claves. Sin costo.</p><div class="cta">Envíanos tu RUC por mensaje directo</div>'),
]
EXTRA = """
.scene{position:absolute;inset:0;padding:300px 80px 340px;display:flex;flex-direction:column;justify-content:center;gap:48px;opacity:0;z-index:1;
 animation:life var(--d) linear var(--a) both}
.scene > *{animation:rise .7s cubic-bezier(.2,.8,.2,1) both}
.scene > *:nth-child(1){animation-delay:calc(var(--a) + .05s)} .scene > *:nth-child(2){animation-delay:calc(var(--a) + .2s)}
.scene > *:nth-child(3){animation-delay:calc(var(--a) + .35s)} .scene > *:nth-child(4){animation-delay:calc(var(--a) + .5s)}
.scene > *:nth-child(5){animation-delay:calc(var(--a) + .65s)}
@keyframes life{0%{opacity:0}4%{opacity:1}94%{opacity:1}100%{opacity:0}}
.scene:last-child{animation-name:lifeend}
@keyframes lifeend{0%{opacity:0}4%{opacity:1}100%{opacity:1}}
@keyframes rise{from{opacity:0;transform:translateY(60px)}to{opacity:1;transform:none}}
.num{font-family:J;font-weight:700;font-size:150px;color:#5FE0E0;line-height:1}
.bar{position:absolute;left:80px;right:80px;top:250px;height:6px;background:rgba(255,255,255,.15);border-radius:6px;z-index:2}
.bar i{display:block;height:100%;background:#5FE0E0;border-radius:6px;animation:grow 24s linear both}
@keyframes grow{from{width:0}to{width:100%}}
"""
html=f"""<html><head><meta charset=utf-8><style>:root{{--w:1080px;--h:1920px;--pad:80px;--fb:300px}}{CSS}{EXTRA}</style></head>
<body><div class="s navy glow" style="padding:0"><div class="bar"><i></i></div>{''.join(SC)}
<div class="foot"><div class="b"><img src="{A}/sym_white.png">@contabilidad360ec</div><div></div></div></div></body></html>"""
async def main():
    out=ROOT/"reel"; out.mkdir(exist_ok=True); (ROOT/"out").mkdir(exist_ok=True); [f.unlink() for f in out.glob("*.png")]
    hp=out/"reel.html"; hp.write_text(html)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto(hp.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i in range(FPS*DUR):
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/FPS})")
            await pg.screenshot(path=str(out/f"f{i:04d}.png"))
        await b.close()
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",str(out/"f%04d.png"),
      "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest","-c:v","libx264","-pix_fmt","yuv420p","-crf","20",
      "-c:a","aac","-movflags","+faststart",str(ROOT/"out"/"r8.mp4")],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","3.5","-i",str(ROOT/"out"/"r8.mp4"),"-frames:v","1",str(ROOT/"out"/"r8_cover.jpg")])
asyncio.run(main())
