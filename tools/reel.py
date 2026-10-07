import asyncio, pathlib, subprocess, sys
from playwright.async_api import async_playwright
sys.path.insert(0,'.')
ROOT=pathlib.Path(__file__).parent; A=(ROOT/"assets").as_uri()
src=open(ROOT/"build_week.py").read(); CSS=src[src.index('CSS = f"""')+10:src.index('"""',src.index('CSS = f"""')+10)]
CSS=CSS.replace("{{","{").replace("}}","}").replace("{A}",A)
FPS=30; DUR=19
# scenes: (start,end,html)
def sc(a,b,html): return f'<div class="scene" style="--a:{a}s;--d:{b-a}s">{html}</div>'
SC = [
 sc(0,4.2,'<div class="tag">Dato tributario</div><h1 style="font-size:104px">¿Qué puede ver cualquiera con el <span class="hl">RUC</span> de tu empresa?</h1>'),
 sc(4.2,7.6,'<div class="num">01</div><h2 style="font-size:84px">Tu historial de cumplimiento ante el <span class="hl">SRI</span></h2>'),
 sc(7.6,11,'<div class="num">02</div><h2 style="font-size:84px">Tus obligaciones societarias en la <span class="hl">Supercías</span></h2>'),
 sc(11,14.4,'<h2 style="font-size:84px">Si la autoridad lo puede ver, <span class="hl">tú también deberías.</span></h2>'),
 sc(14.4,19,f'<img src="{A}/sym_white.png" style="width:200px"><div class="tag">Diagnóstico preventivo</div><h2 style="font-size:80px">Lo revisamos por ti en <span class="hl">24 horas.</span></h2><p class="lead">Solo con tu RUC. Sin claves. Sin costo.</p><div class="cta">Envíanos tu RUC por DM</div>'),
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
.bar i{display:block;height:100%;background:#5FE0E0;border-radius:6px;animation:grow 19s linear both}
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
      "-c:a","aac","-movflags","+faststart",str(ROOT/"out"/"r1.mp4")],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","3.5","-i",str(ROOT/"out"/"r1.mp4"),"-frames:v","1",str(ROOT/"out"/"r1_cover.jpg")])
asyncio.run(main())
