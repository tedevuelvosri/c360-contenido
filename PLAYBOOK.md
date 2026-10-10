# Contabilidad360 · Playbook de contenido semanal

Instrucciones para la sesión que crea y programa cada semana el contenido de Instagram (@contabilidad360ec) y LinkedIn (perfil personal de la socia fundadora) vía Metricool.

## Cuentas y herramientas
- Metricool blogId **7284119**, zona horaria **America/Guayaquil**. Redes conectadas: Instagram y LinkedIn (perfil personal de la fundadora).
- Imágenes y videos se alojan en este repo público y se pasan a Metricool como URL raw:
  `https://raw.githubusercontent.com/tedevuelvosri/c360-contenido/main/<carpeta>/<archivo>`
- Carpeta por semana: `semana-AAAA-MM-DD/` (fecha del miércoles que abre la semana).
- Render: `tools/build_week.py` (posts 1080x1350, historias 1080x1920) y `tools/reel.py` (Reel MP4 1080x1920, 30 fps, animado con CSS). Editar los diccionarios `P`, `S` y la lista `SC` y ejecutar. Salida en `tools/out/`. Fuentes y logos en `tools/assets/`.
- Playwright y ffmpeg están instalados. Siempre revisar visualmente cada imagen (que nada se salga ni pise el pie de página) antes de publicar.

## Cadencia (semana de miércoles a martes)
| Día | Instagram | LinkedIn |
|---|---|---|
| Miércoles | 10:00 Reel | 08:40 mismo video, texto adaptado |
| Jueves | 10:00 Historia | — |
| Viernes | 10:00 Carrusel (4 láminas) | 08:40 mismo carrusel como documento PDF |
| Sábado | 11:00 Historia | — |
| Domingo | 18:00 Historia | — |
| Lunes | 10:00 Carrusel (4 láminas) | 08:40 mismo carrusel como documento PDF |
| Martes | 10:00 Historia (adelanto del carrusel del lunes, “míralo en el perfil”) | — |

Metricool: Instagram `instagramData.type` = REEL / POST / STORY, `autoPublish: true`. Historias sin texto. Reel con `videoThumbnailUrl` (portada JPG). LinkedIn: carruseles con `linkedinData.publishImagesAsPDF: true` y `documentTitle`. No hay herramienta para borrar: para frenar algo, `updateScheduledPost` con `draft: true` y el contenido completo.

## Posicionamiento y tono (brandbook vigente)
- Frase central: **“Dirección contable y tributaria estratégica para tu empresa.”**
- Público: gerentes, directores, dueños de pymes y medianas empresas, profesionales de alto ticket en Quito/Ecuador.
- Tono consultivo, profesional, directo. Hablar de rentabilidad, flujo de caja, mitigación de riesgos, ahorro tributario legal, prevención de glosas y contingencias.
- Pilares: Rigor corporativo · Enfoque preventivo · Visión regional (EC · PE · CO) · Claridad sin jerga.
- Diferencial: la socia fundadora — doble maestría, trayectoria en corporaciones multinacionales, normativa de Ecuador, Perú y Colombia, atención sénior directa sin intermediarios junior, CFO externo.
- Servicios: BPO contable bajo NIIF · Tributación estratégica SRI (IVA, retenciones, ATS, renta) · Nómina y gestión IESS · Cumplimiento Supercías (balances, informe de comisario).
- Gancho: **diagnóstico preventivo sin costo**: solo con el RUC (consulta pública), sin claves, reporte en 24 h con alertas de riesgo, posibles multas y oportunidades de ahorro.

## Prohibido
- Mencionar “5 contadoras”, “+25 años”, tamaño de equipo o cualquier afirmación que no resista una revisión en LinkedIn.
- Presentarse como tramitador, vendedor de firma electrónica o “trámites digitales”. Nada de precios bajos ni “contabilidad barata”.
- Publicar precios, salvo que Camilo lo pida.
- **Número de WhatsApp**: no ponerlo hasta que Camilo dé el nuevo. CTA siempre: “Envíanos tu RUC por mensaje directo” (Instagram) / “escríbeme” (LinkedIn).
- Inventar anécdotas, clientes, cifras o testimonios. En LinkedIn se escribe en primera persona como la fundadora, pero solo con hechos del brandbook.
- Datos tributarios sin verificar. Fechas, porcentajes, montos o cambios normativos: confirmar con búsqueda web en fuentes oficiales (sri.gob.ec, supercias.gob.ec, iess.gob.ec) o medios serios antes de publicarlos. Si no se puede verificar, no publicar el dato.

## Diseño
Colores: navy #0B1F6E (degradado #071454→#132A8C), turquesa #5FE0E0, azul #2E8FD1, off-white #F6F8FB. Tipos: Montserrat (títulos), JetBrains Mono (etiquetas, números), Inter (texto). Portada y cierre en navy, láminas interiores en off-white con tarjetas. Pie con símbolo + @contabilidad360ec. Historias con margen inferior de 300 px (zona segura).

## Calendario SRI (historias de recordatorio)
IVA y retenciones mensuales vencen según el 9.º dígito del RUC: 1→10, 2→12, 3→14, 4→16, 5→18, 6→20, 7→22, 8→24, 9→26, 0→28. Si cae en fin de semana o feriado nacional, pasa al siguiente día hábil. Revisar feriados de Ecuador del mes (búsqueda web) antes de publicar fechas. La historia del jueves puede mostrar los vencimientos de esa semana.

## Temas ya publicados (no repetir; ampliar esta lista cada semana)
- Sem. 07-oct: Presentación de marca · Diagnóstico preventivo (3 pasos) · 5 contingencias frecuentes (ATS vs IVA, gastos sin sustento, retenciones, Supercías atrasada, nómina vs IESS) · Historias: calendario IVA octubre, noveno dígito del RUC, diagnóstico, contingencia #1.
- Sem. 14-oct: Reel “¿Qué puede ver cualquiera con el RUC de tu empresa?” · Carrusel “Qué mira un banco antes de un crédito / contabilidad para declarar vs para decidir” · Carrusel “¿Contador o CFO externo?” · Historias: vencimientos semana (dígitos 4-6), pregunta flujo de caja, qué revisa el diagnóstico, adelanto CFO.
- Sem. 21-oct: Reel “Tu Impuesto a la Renta se decide antes del 31 de diciembre” (cierre fiscal: proyectar utilidad, comprobantes válidos, conciliar retenciones/crédito tributario) · Carrusel “Conciliación bancaria: señales de alerta” · Carrusel “5 indicadores financieros para gerencia” (márgenes bruto/neto, liquidez corriente, días de cobro/pago) · Historias: vencimientos dígitos 7-0 (24-oct sábado → lun 26), pregunta renta si el año cerrara hoy, mito “si el SRI no me notificó estoy bien”, adelanto indicadores.

## Ideas de temas pendientes
Décimo tercer sueldo (verificar fecha) · Gastos personales deducibles (verificar reglas vigentes) · Convenios de doble tributación EC-PE-CO · Qué es una glosa del SRI · Informe de comisario · Fondos de reserva · Flujo de caja proyectado · Errores al facturar electrónicamente (desde el punto de vista contable, sin vender firmas) · Preparación ante una fiscalización.

## Cierre de cada ejecución
1. Verificar con `getScheduledPosts` que todo quedó programado (fechas, tipo, draft false).
2. Hacer commit y push del contenido y de este playbook actualizado (lista de temas publicados).
3. Enviar a Camilo un resumen corto en español: tabla día/tipo/tema y las láminas en hojas de contacto.
