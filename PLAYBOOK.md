# Contabilidad360 · Playbook de contenido semanal

Instrucciones para la sesión que crea y programa cada semana el contenido de Instagram (@contabilidad360ec) vía Metricool. LinkedIn ya no se usa.

## Cuentas y herramientas
- Metricool blogId **7284119**, zona horaria **America/Guayaquil**. Redes conectadas: Instagram y LinkedIn (perfil personal de la fundadora).
- Imágenes y videos se alojan en este repo público y se pasan a Metricool como URL raw:
  `https://raw.githubusercontent.com/tedevuelvosri/c360-contenido/main/<carpeta>/<archivo>`
- Carpeta por semana: `semana-AAAA-MM-DD/` (fecha del miércoles que abre la semana).
- Render: `tools/build_week.py` (posts 1080x1350, historias 1080x1920) y `tools/reel.py` (Reel MP4 1080x1920, 30 fps, animado con CSS). Editar los diccionarios `P`, `S` y la lista `SC` y ejecutar. Salida en `tools/out/`. Fuentes y logos en `tools/assets/`.
- Playwright y ffmpeg están instalados. Siempre revisar visualmente cada imagen (que nada se salga ni pise el pie de página) antes de publicar.

## Límite de Metricool (plan gratuito): 20 publicaciones al mes
- Metricool gratis permite **20 publicaciones publicadas por mes natural**, (una misma pieza en dos redes cuenta 2). Las historias cuentan. Las publicaciones que fallan no cuentan. Se reinicia el día 1.
- Antes de programar, contar con `getScheduledPosts` todo lo **publicado o pendiente no borrador** del mes natural y no pasar de **19** (1 de margen).
- Una semana que cruza de mes cuenta para cada mes según la fecha de cada pieza.

## Cadencia (semana de miércoles a martes) — 4 publicaciones por semana, solo Instagram
**LinkedIn ya no se usa (decisión de Camilo, 16-nov-2026): no programar nada en LinkedIn.**
| Día | Instagram |
|---|---|
| Miércoles | 10:00 Reel |
| Jueves | 10:00 Historia (calendario SRI de la semana o recordatorio clave) |
| Sábado | 11:00 Historia (pregunta, mito o adelanto del carrusel del lunes) |
| Lunes | 10:00 Carrusel (4-5 láminas) |

En un mes con 5 semanas se puede llegar a 20: en ese caso se omite la historia del sábado de la última semana.

Metricool: Instagram `instagramData.type` = REEL / POST / STORY, `autoPublish: true`. Historias sin texto. Reel con `videoThumbnailUrl` (portada JPG). LinkedIn: carruseles con `linkedinData.publishImagesAsPDF: true` y `documentTitle`. No hay herramienta para borrar: para frenar algo, `updateScheduledPost` con `draft: true` y el contenido completo.

## Posicionamiento y tono (brandbook vigente)
- Frase central: **“Dirección contable y tributaria estratégica para tu empresa.”**
- Público: gerentes, directores, dueños de pymes y medianas empresas, profesionales de alto ticket en Quito/Ecuador.
- Tono consultivo, profesional, directo. Hablar de rentabilidad, flujo de caja, mitigación de riesgos, ahorro tributario legal, prevención de glosas y contingencias.
- Pilares: Rigor corporativo · Enfoque preventivo · Visión regional (EC · PE · CO) · Claridad sin jerga.
- Diferencial: la socia fundadora (Cecilia Bermeo) — CPA, Magíster en Contabilidad y Auditoría, especialista en Tributación (UTPL), más de 25 años de experiencia, ex Directora Financiera-Contable de un grupo con operaciones en Ecuador, Perú y Colombia; atención sénior directa, CFO externo. **No decir “doble maestría” ni “años en corporaciones multinacionales”** (no consta en su hoja de vida).
- Servicios: BPO contable bajo NIIF · Tributación estratégica SRI (IVA, retenciones, ATS, renta) · Nómina y gestión IESS · Cumplimiento Supercías (balances, informe de comisario).
- Gancho: **diagnóstico preventivo sin costo**: solo con el RUC (consulta pública), sin claves, reporte en 24 h con alertas de riesgo, posibles multas y oportunidades de ahorro.

## Prohibido
- Mencionar “5 contadoras”, años de experiencia de un equipo, tamaño de equipo (los +25 años son solo de la fundadora) o cualquier afirmación que no resista una revisión en LinkedIn.
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
- Sem. 28-oct: Reel “El décimo tercer sueldo no debería sorprenderte en diciembre” (período 1 dic–30 nov, 1/12, pago hasta 24 dic, mensualizado, provisionar) · Carrusel “Llegó una notificación del SRI: qué hacer y qué evitar” · Carrusel “Flujo de caja proyectado: cómo armarlo y pagos que se olvidan” · Historias: calendario noviembre dígitos 1-5 (14-nov sábado → lun 16), pregunta décimo tercero provisionado, mito “la contabilidad solo sirve para pagar impuestos”, adelanto flujo de caja.
- Sem. 04-nov: Reel “Fondos de reserva: lo que todo empleador debe tener claro” (después del primer año, 8,33%, rol o IESS según elija el trabajador) · Carrusel “¿Qué es una glosa del SRI?” (definición, 4 orígenes frecuentes) · Carrusel “Decisión 578 CAN: dónde tributa cada renta” (regla de la fuente, dividendos, intereses, servicios personales, transporte) · Historias: calendario noviembre dígitos 6-0 (20-nov sin jornada por Decreto 507 → “declara antes”; 22 dom → lun 23; 28 sáb → lun 30), pregunta gastos que podría objetar el SRI, ¿sabías que? IVA válido solo con pago simultáneo desde jun-2026 (Res. NAC-DGERCGC26-00000016), adelanto Decisión 578.
- Sem. 11-nov: Reel “Un mes sin ventas no es un mes sin obligaciones” (declaración de IVA en cero, art. 158 Reglamento LRTI; multas por presentación tardía aplican a declaraciones en cero) · Carrusel “Décimo cuarto sueldo: dos regiones, dos calendarios” (1 SBU = USD 482 en 2026, proporcional; Costa/Galápagos 1 mar–fin feb, pago hasta 15 mar; Sierra/Amazonía 1 ago–31 jul, pago hasta 15 ago) · Carrusel “Siete años: lo que tu empresa debe conservar” (art. 41 Reglamento de Comprobantes de Venta; facturas, liquidaciones, NC/ND, retenciones, guías) · Historias: vencimientos semana dígitos 2-4 (14-nov sáb → lun 16), pregunta ¿encontrarías una factura de hace 5 años?, mito “el décimo cuarto se paga igual en todo el país”, adelanto siete años.
- Sem. 18-nov: Reel “Más de USD 500 en efectivo: un gasto que el SRI no reconoce” (bancarización, art. 103 LRTI: sobre USD 500 por sistema financiero o se pierde deducibilidad y crédito tributario IVA; se mide por operación, no por pago) · Carrusel “Cuentas por cobrar viejas: lo que la ley permite provisionar” (1% anual créditos del ejercicio, tope 10% cartera, art. 10 num. 11 LRTI; baja según art. 28 num. 3 Reglamento: 2 años registrado, 3 años vencido, prescripción, quiebra/insolvencia o sociedad cancelada) · Carrusel “Antes de una fiscalización: 4 preguntas que tu contabilidad debe responder hoy” (cuadre declaraciones vs EEFF, sustento de gastos, retenciones, expediente por período) · Historias: vencimientos dígitos 6-8 (20-nov jornada suspendida Decreto 507 → declara antes; 22 dom → lun 23; 24 mar), pregunta cartera con más de un año sin cobrar, mito “con factura el gasto en efectivo es deducible”, adelanto fiscalización.
- Sem. 25-nov: Reel “Tu inventario en libros no siempre es el que hay en bodega” (toma física vs kárdex antes del 31-dic, diferencias documentadas con acta, NIIF: menor entre costo y valor neto realizable; sin afirmaciones tributarias sobre bajas) · Carrusel “Anular una factura electrónica: plazos y reglas vigentes” (Res. NAC-DGERCGC25-00000017: anulación en línea hasta el día 7 del mes siguiente; después solo con NC en casos del Reglamento; consumidor final no se anula ni admite NC desde 1-ene-2026; NC/ND/retenciones requieren aceptación del receptor en 5 días hábiles) · Carrusel “Presupuesto 2027: 4 decisiones antes de enero” (base en cifras reales cerradas; metas por línea, estructura de costos, flujo mensual, revisión real vs presupuesto) · Historias: vencimientos dígitos 9-0 (26 jue; 28 sáb → lun 30), adelanto dígito 1 → jue 10-dic, pregunta ¿cuándo contaste tu inventario?, mito “una factura electrónica se puede anular cuando sea”, adelanto presupuesto 2027.

## Temas prioritarios diciembre 2026 – febrero 2027 (documento de Camilo, 16-nov)
Usar en este orden aproximado. Verificar cada dato con fuente oficial o medio serio antes de publicar.
- **Ya publicado (20-nov):** carrusel “Noviembre a febrero: checklist de obligaciones” (semana-2026-11-18/ck_*). No repetir el checklist completo; sí profundizar en cada punto.
- **Diciembre:** décimo tercer sueldo hasta el 24-dic y registro en el MDT (enero dígitos 1-5, luego 6-0); cierre contable y revisión de comprobantes electrónicos.
- **Diciembre — transporte (prioridad):** Res. NAC-DGERCGC26-00000024 (13-jul-2026) y su reforma NAC-DGERCGC26-00000028 (3-ago-2026). Desde el 1-ene-2027 se eliminan los puntos de emisión de socios: el socio factura solo a la operadora y la operadora factura al cliente final. Aplica a carga pesada y liviana, escolar e institucional, turístico, mixto y alternativo-excepcional; no a taxis. Si una empresa recibe factura de un socio y no de la operadora, el gasto deja de ser deducible. Confirmar en el texto de las resoluciones antes de publicar.
- **Diciembre/enero — facturación electrónica 2027:** RUC del proveedor tecnológico en la información adicional del comprobante (Res. NAC-DGERCGC26-00000027; el SRI publica listado de proveedores autorizados); transmisión inmediata. (Anulación hasta el día 7 y consumidor final ya publicados el 27-nov.)
- **Enero — catastro RIMPE:** actualización en los primeros días hábiles de enero: de Negocio Popular a Emprendedor si superó USD 20.000 de ingresos; exclusión al Régimen General si superó USD 300.000 o cumplió 3 años en RIMPE Emprendedor; depuración a mitad de año desde el 1-jul. Verificar.
- **Enero:** IVA semestral (10 al 28 según dígito); Anexo RDEP desde el 21-ene hasta el 7-feb; predial Quito con descuento por pronto pago (en 2026: 10% hasta el 15-ene; confirmar 2027); décimos: solicitud de acumulación/mensualización hasta el 15-ene.
- **Febrero:** REBEFICS 10 al 28 según dígito; Anexo de gastos personales 10 al 28; registro décimo tercero dígitos 6-0.
- **No publicar:** “tercera cuota del anticipo sobre utilidades no distribuidas en noviembre” (en 2026 se pagó en agosto o en cuotas agosto–octubre, Res. NAC-DGERCGC26-00000026); “reporte de socios extranjeros a la Supercías hasta el 28 de febrero” (no verificado).
- **Piezas listas sin publicar (se pasaron a borrador por el límite de noviembre; se pueden reprogramar en diciembre sin rediseñar):** carrusel “Antes de una fiscalización: 4 preguntas” (semana-2026-11-18/w7b_*), carrusel “Presupuesto 2027: 4 decisiones antes de enero” (semana-2026-11-25/w8b_*). Ambos tienen texto IG y LinkedIn en los borradores de Metricool del 23 y 30 de noviembre.

- **Ajuste 16-nov (límite de Metricool):** de las semanas 18-nov y 25-nov solo se publican en Instagram el reel de bancarización (18), el carrusel checklist nov–feb (20, reemplazó a “cuentas por cobrar viejas”), el reel de inventario (25) y el carrusel de anulación de facturas (27). Quedaron en borrador sin publicar: cuentas por cobrar viejas, fiscalización, presupuesto 2027, todas las historias del 17-nov al 1-dic y todo LinkedIn desde el 18-nov. Los temas en borrador se pueden usar más adelante.

## Ideas de temas pendientes
Gastos personales deducibles / rebaja de IR (verificar reglas vigentes) · Informe de comisario (verificar si sigue siendo obligatorio tras reformas a la Ley de Compañías) · Errores al facturar electrónicamente (ya se cubrió anulación de comprobantes; queda p. ej. datos del cliente, transmisión) · Preparación ante una fiscalización (ya se cubrieron “notificación del SRI”, “glosa” y “4 preguntas antes de una fiscalización”; ampliar sin repetir) · Convenios bilaterales de doble tributación de Ecuador (ya se cubrió la Decisión 578 CAN) · Calendario SRI de diciembre (dígitos 1-5 y 6-0; revisar feriados de diciembre) · Caducidad de la facultad determinadora del SRI (art. 94 Código Tributario: fuentes discrepan entre 3 y 4 años tras reformas; verificar en texto oficial antes de publicar) · Proyección de gastos personales de empleados (verificado 2026: rebaja 18% sobre el menor entre gastos y canastas; canasta ene-2026 USD 821,80; fechas de entrega al empleador por confirmar) · Nota: la anulación de comprobantes tiene fuentes que discrepan sobre si el día 7 se corre al siguiente hábil; no publicar ese detalle sin texto oficial.

## Cierre de cada ejecución
0. Revisar si hubo publicaciones con estado ERROR la semana anterior (p. ej. LinkedIn “authentication failure”) y avisarlo a Camilo en el resumen.
1. Verificar con `getScheduledPosts` que todo quedó programado (fechas, tipo, draft false).
2. Hacer commit y push del contenido y de este playbook actualizado (lista de temas publicados).
3. Enviar a Camilo un resumen corto en español: tabla día/tipo/tema y las láminas en hojas de contacto.
