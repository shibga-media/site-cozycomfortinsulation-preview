#!/usr/bin/env python3
"""Cozy Comfort Insulation preview site. Static, EN at root, ES in /es/ (same approach as the BHTS hair site:
separate URL per language, EN | ES bar at the top, hreflang pairs). Run: python3 build.py -> docs/"""
import os, shutil, html
INDEXABLE = False          # flip to True only after Shib approves
PHONE_DISPLAY, PHONE_TEL = "(818) 927-7494", "+18189277494"
LIC = "1140834"
ROOT = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(ROOT, "docs")

SERVICES = [
 ("attic", "Attic Insulation", "Aislamiento de ático",
  "The biggest comfort upgrade in most California homes. We measure what you have, fix gaps and damaged areas, and bring the attic up to current energy-code levels.",
  "La mejora de comodidad más importante en la mayoría de los hogares de California. Medimos lo que tiene, corregimos huecos y áreas dañadas y llevamos el ático al nivel que exige el código de energía."),
 ("blown", "Blown-In Insulation", "Aislamiento soplado",
  "Loose-fill cellulose or fiberglass blown evenly over the attic floor and into closed cavities, with no tearing out of walls or ceilings.",
  "Celulosa o fibra de vidrio suelta, soplada de manera uniforme sobre el piso del ático y dentro de cavidades cerradas, sin romper paredes ni techos."),
 ("foam", "Spray Foam Insulation", "Espuma en aerosol",
  "Open-cell and closed-cell spray foam that insulates and air-seals in one step. Ideal for garages, rooms over garages, and hard-to-reach areas.",
  "Espuma de celda abierta y de celda cerrada que aísla y sella el aire en un solo paso. Ideal para garajes, cuartos sobre el garaje y zonas de difícil acceso."),
 ("crawl", "Crawl Space Insulation", "Aislamiento de espacio de acceso",
  "Insulation and moisture control under the floor to cut drafts, keep floors warmer, and help protect against damp and pests.",
  "Aislamiento y control de humedad bajo el piso para reducir corrientes de aire, mantener los pisos más cálidos y ayudar a prevenir la humedad y las plagas."),
 ("removal", "Insulation Removal & Replacement", "Retiro y reemplazo de aislamiento",
  "Old, wet, matted, or rodent-damaged insulation taken out, the area cleaned and treated, and fresh insulation installed.",
  "Retiramos el aislamiento viejo, mojado, aplastado o dañado por roedores, limpiamos y tratamos el área e instalamos aislamiento nuevo."),
 ("radiant", "Radiant Barrier Installation", "Instalación de barrera radiante",
  "A reflective layer under the roof that bounces away the sun's heat, keeping the attic and the rooms below noticeably cooler in summer.",
  "Una capa reflectante bajo el techo que rechaza el calor del sol y mantiene el ático y las habitaciones de abajo mucho más frescos en verano."),
]

P = {  # page strings: (en, es)
 "nav": [("Home", "Inicio", "index.html"), ("Services", "Servicios", "services.html"), ("About", "Nosotros", "about.html"), ("Contact", "Contacto", "contact.html")],
 "cta": ("Get a free quote", "Cotización gratis"),
 "call": ("Call", "Llame al"),
 "lic": (f"CSLB C-2 Licensed #{LIC}", f"Contratista con licencia CSLB C-2 #{LIC}"),
 "trust": [("Licensed", f"CSLB C-2 #{LIC}", "Con licencia", f"CSLB C-2 #{LIC}"), ("Insured", "General liability + workers' comp", "Asegurados", "Responsabilidad civil y compensación laboral"),
           ("Free estimates", "No pressure, no obligation", "Cotización gratis", "Sin presión, sin compromiso"), ("California-wide", "Homes and businesses", "En todo California", "Hogares y negocios")],
 "title": {
   "index": ("Insulation Contractor in California | Cozy Comfort Insulation", "Contratista de aislamiento en California | Cozy Comfort Insulation"),
   "services": ("Insulation Services | Cozy Comfort Insulation", "Servicios de aislamiento | Cozy Comfort Insulation"),
   "about": ("About Us | Cozy Comfort Insulation", "Nosotros | Cozy Comfort Insulation"),
   "contact": ("Contact & Free Quote | Cozy Comfort Insulation", "Contacto y cotización gratis | Cozy Comfort Insulation")},
 "desc": {
   "index": ("Licensed California insulation contractor. Attic, blown-in, spray foam, crawl space, removal and radiant barrier. Free estimates. Call (818) 927-7494.",
             "Contratista de aislamiento con licencia en California. Ático, soplado, espuma, espacio de acceso, retiro y barrera radiante. Cotización gratis. Llame al (818) 927-7494."),
   "services": ("Attic insulation, blown-in, spray foam, crawl space, removal and replacement, and radiant barrier. Licensed California contractor.",
                "Aislamiento de ático, soplado, espuma en aerosol, espacio de acceso, retiro y reemplazo, y barrera radiante. Contratista con licencia en California."),
   "about": ("Cozy Comfort Insulation is a licensed, insured California insulation contractor focused on comfort, lower energy bills and clean work.",
             "Cozy Comfort Insulation es un contratista de aislamiento con licencia y seguro en California, enfocado en comodidad, facturas de energía más bajas y trabajo limpio."),
   "contact": ("Get a free insulation quote. Chat with us or call (818) 927-7494.", "Pida su cotización gratis de aislamiento. Chatee con nosotros o llame al (818) 927-7494.")},
}

def t(pair, es): return pair[1] if es else pair[0]

CSS = """
:root{--blue:#2f7fc1;--blue-d:#1f5f96;--orange:#f4a030;--green:#2e9f4f;--ink:#1b2a3a;--soft:#f5f8fb;--line:#dfe7ee}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:#fff}
img{max-width:100%;height:auto}a{color:var(--blue-d)}h1,h2,h3{line-height:1.2;margin:0 0 .5em}h1{font-size:clamp(30px,5vw,50px)}h2{font-size:clamp(25px,3.4vw,36px)}h3{font-size:20px}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.lang{background:var(--ink);color:#fff;font:600 13px/1 system-ui,sans-serif}.lang .wrap{display:flex;justify-content:space-between;align-items:center;padding:8px 20px}
.lang a{color:#fff;text-decoration:none;padding:4px 8px;border-radius:6px}.lang b{background:var(--orange);color:var(--ink);padding:4px 8px;border-radius:6px}.lang .l{opacity:.85;font-weight:500}
header.top{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}header.top .wrap{display:flex;align-items:center;gap:20px;padding:10px 20px}
.logo img{height:62px;width:auto;display:block}nav{margin-left:auto;display:flex;gap:6px;flex-wrap:wrap;align-items:center}nav a{color:var(--ink);text-decoration:none;font-weight:600;padding:8px 12px;border-radius:8px}nav a:hover,nav a.on{background:var(--soft);color:var(--blue-d)}
.btn{display:inline-block;background:var(--orange);color:var(--ink)!important;font-weight:800;border-radius:999px;padding:14px 26px;text-decoration:none;border:0;cursor:pointer;font-size:17px}.btn:hover{filter:brightness(.95)}
.btn.line{background:transparent;border:2px solid #fff;color:#fff!important}.btn.blue{background:var(--blue);color:#fff!important}
.hero{background:linear-gradient(135deg,var(--blue-d),var(--blue) 60%,#4a97d6);color:#fff;padding:72px 0 80px}.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center}
.hero p.lead{font-size:20px;opacity:.95;max-width:560px}.hero .acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.hero .card{background:#fff;border-radius:18px;padding:22px;color:var(--ink);box-shadow:0 14px 40px rgba(0,0,0,.25)}.hero .card img{width:100%;max-width:300px;display:block;margin:0 auto}
.trust{background:var(--soft);border-bottom:1px solid var(--line)}.trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:22px 20px}.trust div{font-size:14px;color:#445}.trust b{display:block;font-size:16px;color:var(--ink)}
section.s{padding:68px 0}section.alt{background:var(--soft)}.sec-h{max-width:680px;margin-bottom:34px}.sec-h p{color:#455;margin:0}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.card2{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px;border-top:5px solid var(--blue)}.card2:nth-child(3n+2){border-top-color:var(--orange)}.card2:nth-child(3n){border-top-color:var(--green)}.card2 p{margin:0 0 14px;color:#445}.card2 a.more{font-weight:700;text-decoration:none}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;counter-reset:st}.steps div{background:#fff;border-radius:16px;padding:24px;border:1px solid var(--line)}.steps div::before{counter-increment:st;content:counter(st);display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--orange);color:var(--ink);font-weight:800;margin-bottom:10px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}ul.ck{list-style:none;padding:0;margin:0}ul.ck li{padding:6px 0 6px 30px;position:relative}ul.ck li::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:800}
details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-bottom:10px}summary{font-weight:700;cursor:pointer}details p{margin:10px 0 0;color:#445}
.cta{background:var(--ink);color:#fff;text-align:center;padding:60px 0}.cta p{opacity:.9;max-width:560px;margin:0 auto 22px}
footer{background:#111c28;color:#c9d5df;padding:36px 0;font-size:15px}footer .wrap{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between}footer a{color:#fff}
.phead{background:var(--soft);padding:44px 0;border-bottom:1px solid var(--line)}
@media(max-width:860px){.hero .wrap,.two{grid-template-columns:1fr}.grid,.steps{grid-template-columns:1fr}.trust .wrap{grid-template-columns:1fr 1fr}.hero{padding:44px 0 52px}nav{margin:0;width:100%}header.top .wrap{flex-wrap:wrap}.logo img{height:52px}nav a{padding:6px 9px}}
"""

def page(slug, es, body):
    pre = "../" if es else ""
    other = ("../" if es else "es/")  # path to the other language root from this page
    en_url = (pre + slug + ".html") if es else slug + ".html"
    es_url = slug + ".html" if es else "es/" + slug + ".html"
    sw_other = ("../" + slug + ".html") if es else ("es/" + slug + ".html")
    nav = "".join(f'<a href="{h}"{" class=on" if h==slug+".html" else ""}>{t((a,b),es)}</a>' for a, b, h in P["nav"])
    cta = t(P["cta"], es)
    robots = '<meta name="robots" content="index,follow">' if INDEXABLE else '<meta name="robots" content="noindex,nofollow">'
    switch = (f'<div class="lang"><div class="wrap"><span class="l">{t(("Licensed California insulation contractor","Contratista de aislamiento con licencia en California"),es)}</span>'
              f'<span><b>{"ES" if es else "EN"}</b> '
              f'<a href="{sw_other}" hreflang="{"en" if es else "es"}" lang="{"en" if es else "es"}">{"English" if es else "Español"}</a></span></div></div>')
    return f"""<!DOCTYPE html><html lang="{'es' if es else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(t(P['title'][slug],es))}</title><meta name="description" content="{html.escape(t(P['desc'][slug],es))}">{robots}
<link rel="alternate" hreflang="en" href="{'../' if es else ''}{slug}.html"><link rel="alternate" hreflang="es" href="{'' if es else 'es/'}{slug}.html"><link rel="alternate" hreflang="x-default" href="{'../' if es else ''}{slug}.html">
<link rel="icon" href="{pre}assets/favicon.png"><link rel="apple-touch-icon" href="{pre}assets/favicon-192.png"><link rel="stylesheet" href="{pre}assets/site.css"></head><body>
{switch}
<header class="top"><div class="wrap"><a class="logo" href="{'index.html'}"><img src="{pre}assets/logo.png" alt="Cozy Comfort Insulation" width="130" height="62"></a><nav>{nav}<a class="btn blue" href="tel:{PHONE_TEL}" style="padding:10px 18px">{t(P['call'],es)} {PHONE_DISPLAY}</a></nav></div></header>
{body}
<footer><div class="wrap"><div><b style="color:#fff">Cozy Comfort Insulation</b><br>{t(P['lic'],es)}<br>{t(("California insulation contractor","Contratista de aislamiento en California"),es)}</div>
<div>{t(('Phone','Teléfono'),es)}: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="#" data-cozy-chat>{cta}</a></div>
<div>© 2026 Cozy Comfort Insulation</div></div></footer>
<script src="{pre}assets/cozy-chat.js" defer></script></body></html>"""

def home(es):
    sv = "".join(f'<div class="card2"><h3>{t((n,nes),es)}</h3><p>{t((d,des),es)}</p><a class="more" href="services.html#{k}">{t(("Learn more","Más información"),es)} →</a></div>' for k, n, nes, d, des in SERVICES)
    trust = "".join(f'<div><b>{t((a,c),es)}</b>{t((b,d),es)}</div>' for a, b, c, d in P["trust"])
    faq = [
     (("How do I know if my insulation needs to be replaced?","¿Cómo sé si mi aislamiento necesita reemplazo?"),("Common signs are rooms that are too hot or cold, high energy bills, drafts, uneven temperatures between floors, or insulation that is wet, flattened, or has been disturbed by pests. We inspect it and tell you plainly what you need.","Las señales comunes son habitaciones demasiado calientes o frías, facturas de energía altas, corrientes de aire, temperaturas desiguales entre pisos, o aislamiento mojado, aplastado o alterado por plagas. Lo inspeccionamos y le decimos con claridad lo que necesita.")),
     (("Is the estimate really free?","¿La cotización es realmente gratis?"),("Yes. Tell us about your home in the chat or call us, and we will give you a free, no-obligation estimate.","Sí. Cuéntenos sobre su casa en el chat o llámenos y le daremos una cotización gratis y sin compromiso.")),
     (("Are you licensed and insured?","¿Tienen licencia y seguro?"),(f"Yes. Cozy Comfort Insulation holds California CSLB C-2 (insulation and acoustical) licence #{LIC} and carries general liability and workers' compensation insurance.",f"Sí. Cozy Comfort Insulation tiene la licencia CSLB C-2 (aislamiento y acústica) de California n.º {LIC} y cuenta con seguro de responsabilidad civil y de compensación laboral.")),
     (("Do I need to leave home during the work?","¿Tengo que salir de casa durante el trabajo?"),("Usually not. Most attic and blown-in jobs are done in a day with you at home. We will tell you ahead of time if a job needs anything different.","Normalmente no. La mayoría de los trabajos de ático y aislamiento soplado se hacen en un día con usted en casa. Le avisaremos con anticipación si un trabajo requiere algo distinto.")),
    ]
    fq = "".join(f"<details><summary>{t(q,es)}</summary><p>{t(a,es)}</p></details>" for q, a in faq)
    return f"""
<section class="hero"><div class="wrap"><div>
<h1>{t(("Stay comfortable all year. Pay less to heat and cool your home.","Comodidad todo el año. Pague menos por calentar y enfriar su hogar."),es)}</h1>
<p class="lead">{t(("Cozy Comfort Insulation installs attic, blown-in, spray foam and crawl space insulation for California homes and businesses. Licensed and insured.","Cozy Comfort Insulation instala aislamiento de ático, soplado, espuma en aerosol y de espacio de acceso en hogares y negocios de California. Con licencia y seguro."),es)}</p>
<div class="acts"><a class="btn" href="#" data-cozy-chat>{t(P['cta'],es)}</a><a class="btn line" href="tel:{PHONE_TEL}">{t(P['call'],es)} {PHONE_DISPLAY}</a></div></div>
<div class="card"><img src="{'../' if es else ''}assets/logo.png" alt="Cozy Comfort Insulation" width="300" height="226"></div></div></section>
<div class="trust"><div class="wrap">{trust}</div></div>
<section class="s"><div class="wrap"><div class="sec-h"><h2>{t(("Our insulation services","Nuestros servicios de aislamiento"),es)}</h2><p>{t(("The right material in the right place, installed properly the first time.","El material correcto en el lugar correcto, instalado bien desde la primera vez."),es)}</p></div><div class="grid">{sv}</div></div></section>
<section class="s alt"><div class="wrap"><div class="sec-h"><h2>{t(("How it works","Cómo trabajamos"),es)}</h2></div><div class="steps">
<div><h3>{t(("Tell us about your home","Cuéntenos sobre su casa"),es)}</h3><p>{t(("Use the chat or call us. Share your name, zip code and the service you need.","Use el chat o llámenos. Comparta su nombre, código postal y el servicio que necesita."),es)}</p></div>
<div><h3>{t(("Free inspection and estimate","Inspección y cotización gratis"),es)}</h3><p>{t(("We check what you have now and give you a clear, written estimate.","Revisamos lo que tiene ahora y le damos una cotización clara por escrito."),es)}</p></div>
<div><h3>{t(("Clean, careful installation","Instalación limpia y cuidadosa"),es)}</h3><p>{t(("Our crew protects your home, does the work, and cleans up before leaving.","Nuestro equipo protege su hogar, hace el trabajo y deja todo limpio antes de irse."),es)}</p></div></div></div></section>
<section class="s"><div class="wrap two"><div><h2>{t(("Why homeowners choose Cozy Comfort","Por qué los propietarios eligen Cozy Comfort"),es)}</h2>
<ul class="ck"><li>{t((f"State-licensed contractor, CSLB C-2 #{LIC}",f"Contratista con licencia estatal, CSLB C-2 n.º {LIC}"),es)}</li><li>{t(("Insured: general liability and workers' compensation","Asegurados: responsabilidad civil y compensación laboral"),es)}</li><li>{t(("Honest recommendations, only the work you need","Recomendaciones honestas, solo el trabajo que necesita"),es)}</li><li>{t(("Clean job sites and respect for your home","Obras limpias y respeto por su hogar"),es)}</li></ul></div>
<div><h2>{t(("Common questions","Preguntas frecuentes"),es)}</h2>{fq}</div></div></section>
<section class="cta"><div class="wrap"><h2>{t(("Ready for a more comfortable home?","¿Listo para un hogar más cómodo?"),es)}</h2><p>{t(("Answer a few quick questions and we will call you at a time that works for you.","Responda unas preguntas rápidas y le llamaremos a la hora que le convenga."),es)}</p><a class="btn" href="#" data-cozy-chat>{t(P['cta'],es)}</a></div></section>"""

def services(es):
    items = "".join(f'<section class="s{" alt" if i%2 else ""}" id="{k}"><div class="wrap"><div class="sec-h" style="margin:0"><h2>{t((n,nes),es)}</h2><p style="font-size:18px">{t((d,des),es)}</p><p style="margin-top:16px"><a class="btn" href="#" data-cozy-chat>{t(P["cta"],es)}</a></p></div></div></section>' for i, (k, n, nes, d, des) in enumerate(SERVICES))
    return f'<div class="phead"><div class="wrap"><h1>{t(("Insulation services","Servicios de aislamiento"),es)}</h1><p>{t(("Six ways we make your home more comfortable and efficient. Every job starts with a free estimate.","Seis maneras de hacer su hogar más cómodo y eficiente. Todo trabajo comienza con una cotización gratis."),es)}</p></div></div>{items}'

def about(es):
    return f"""<div class="phead"><div class="wrap"><h1>{t(("About Cozy Comfort Insulation","Acerca de Cozy Comfort Insulation"),es)}</h1></div></div>
<section class="s"><div class="wrap two"><div><p>{t(("We are a licensed California insulation contractor. Our name is our promise: a home that is cozy and comfortable in every season, with energy bills that make sense.","Somos un contratista de aislamiento con licencia en California. Nuestro nombre es nuestra promesa: un hogar acogedor y cómodo en cualquier estación, con facturas de energía razonables."),es)}</p>
<p>{t(("We keep it simple. We look at your home, tell you honestly what it needs, quote it clearly, and do the work carefully. No pressure and no surprises.","Lo hacemos simple. Revisamos su casa, le decimos con honestidad lo que necesita, cotizamos con claridad y hacemos el trabajo con cuidado. Sin presión y sin sorpresas."),es)}</p>
<ul class="ck"><li>{t((f"California CSLB C-2 licence #{LIC}",f"Licencia CSLB C-2 de California n.º {LIC}"),es)}</li><li>{t(("General liability and workers' compensation insurance","Seguro de responsabilidad civil y compensación laboral"),es)}</li><li>{t(("Free inspections and estimates","Inspecciones y cotizaciones gratis"),es)}</li></ul>
<p><a class="btn" href="#" data-cozy-chat>{t(P['cta'],es)}</a></p></div>
<div class="card2" style="text-align:center"><img src="{'../' if es else ''}assets/logo.png" alt="Cozy Comfort Insulation" width="300" height="226" style="max-width:300px"></div></div></section>"""

def contact(es):
    return f"""<div class="phead"><div class="wrap"><h1>{t(("Contact us","Contáctenos"),es)}</h1><p>{t(("The fastest way: tell us a little about your project and pick a time. We will call you.","La forma más rápida: cuéntenos un poco sobre su proyecto y elija una hora. Nosotros le llamamos."),es)}</p></div></div>
<section class="s"><div class="wrap two"><div class="card2"><h2>{t(("Free quote chat","Chat para cotización gratis"),es)}</h2><p>{t(("It takes about a minute: name, phone, email, zip code, service and the best time to call.","Toma cerca de un minuto: nombre, teléfono, correo, código postal, servicio y la mejor hora para llamar."),es)}</p><a class="btn" href="#" data-cozy-chat>{t(P['cta'],es)}</a></div>
<div class="card2"><h2>{t(("Call us","Llámenos"),es)}</h2><p style="font-size:26px;font-weight:800"><a href="tel:{PHONE_TEL}" style="text-decoration:none">{PHONE_DISPLAY}</a></p><p>{t((f"Licensed California contractor, CSLB C-2 #{LIC}.",f"Contratista con licencia en California, CSLB C-2 n.º {LIC}."),es)}</p></div></div></section>"""

def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + "/es"); shutil.copytree(ROOT + "/assets", OUT + "/assets")
    open(OUT + "/assets/site.css", "w").write(CSS)
    for es in (False, True):
        d = OUT + ("/es" if es else "")
        for slug, fn in (("index", home), ("services", services), ("about", about), ("contact", contact)):
            open(f"{d}/{slug}.html", "w").write(page(slug, es, fn(es)))
    open(OUT + "/robots.txt", "w").write("User-agent: *\n" + ("Allow: /\n" if INDEXABLE else "Disallow: /\n"))
    print("built", OUT)
main()
