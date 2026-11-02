# ERTEC · Simulacro de Institucionalización de Cargos 2027-2029

Simulacro del examen de competencia de la **Convocatoria Pública N° 0001/2026**
(Ministerio de Educación · Sistema Educativo Plurinacional). Aplicación web estática: HTML + CSS + JavaScript, sin dependencias ni compilación.

## Estructura del proyecto

```
ertec/
├── index.html · login.html · exam.html · results.html · history.html   Páginas (solo marcado HTML)
├── manifest.json · sw.js                                                PWA: instalable y funciona sin internet
├── assets/
│   ├── css/   base · animations · components · layout · pages/          Estilos por responsabilidad
│   ├── js/    core/ (utils, storage, config, modes, fx, timer, sound)   Lógica compartida
│   │          pages/ (login, index, exam, results, history)             Lógica de cada página
│   └── icons/
├── data/
│   ├── config.json             Convocatoria: cargos, costos, cronograma, perfiles de examen, bibliografías y qué rinde cada cargo
│   └── bib/                    UN JSON por norma o libro (131 archivos) ← aquí van tus preguntas
│       ├── normativa_general/      8 archivos · iguales para todos los cargos
│       ├── normativa_especifica/   48 archivos · reglamentos y resoluciones según el cargo
│       └── tecnico_pedagogico/     75 archivos · libros, informes y normas técnicas según el cargo
├── docs/
│   ├── FORMATO-PREGUNTAS.md        Cómo escribir las preguntas
│   └── BIBLIOGRAFIA-POR-CARGO.md   Qué archivos rinde cada cargo
└── tools/                      validar_bancos.py · sync_bancos.py
```

## Bibliografía: documento «Bibliografía V4» del Ministerio de Educación
Cada cargo tiene 3 áreas: **normativa general** (las mismas 8 normas), **normativa específica** y **técnico pedagógico**.
Cada norma o libro que aparece en el documento es un archivo JSON propio; si varios cargos la comparten, es el mismo archivo.
La lista exacta por cargo está en `docs/BIBLIOGRAFIA-POR-CARGO.md`.

### Tus 16 normativas anteriores: todas se reutilizan
Las 16 normativas de la lista que te pasó tu contacto aparecen en la Bibliografía V4. Sus preguntas ya están cargadas en estos archivos:

| # | Normativa de tu lista de 16 | Archivo nuevo | Cargos que la rinden | Preguntas |
|---|---|---|---|---|
| 1 | Constitución Política del Estado | `normativa_general/ng01_constitucion_politica_del_estado.json` | 33 de 33 | 1 |
| 2 | Ley N° 070 de la Educación "Avelino Siñani–Elizardo Pérez" | `normativa_general/ng02_ley_070_avelino_sinani_elizardo_perez.json` | 33 de 33 | 9 |
| 3 | Ley N° 045 Contra el Racismo y Toda Forma de Discriminación | `normativa_general/ng03_ley_045_contra_el_racismo_y_la_discriminacion.json` | 33 de 33 | 0 |
| 4 | Ley N° 348 Integral para garantizar a las mujeres una vida libre de violencia | `normativa_general/ng04_ley_348_vida_libre_de_violencia.json` | 33 de 33 | 5 |
| 5 | Ley N° 548 Código Niña, Niño y Adolescente | `normativa_general/ng05_ley_548_codigo_nina_nino_adolescente.json` | 33 de 33 | 8 |
| 6 | Ley N° 223 General para Personas con Discapacidad | `normativa_general/ng06_ley_223_personas_con_discapacidad.json` | 33 de 33 | 87 |
| 7 | Ley N° 1178 de Administración y Control Gubernamentales | `normativa_general/ng07_ley_1178_administracion_y_control_gubernamentales.json` | 33 de 33 | 0 |
| 8 | Ley N° 004 de Lucha Contra la Corrupción, Enriquecimiento Ilícito e Investigac | `normativa_general/ng08_ley_004_lucha_contra_la_corrupcion.json` | 33 de 33 | 0 |
| 9 | Decreto Supremo N° 4688 Reglamento del Escalafón Nacional del Servicio de Educ | `normativa_especifica/ne02_ds_4688_reglamento_escalafon_nacional.json` | 23 de 33 | 132 |
| 10 | Resolución Suprema N° 212414 Reglamento de Faltas y Sanciones del Magisterio ( | `normativa_especifica/ne04_rs_212414_reglamento_faltas_y_sanciones.json` | 23 de 33 | 137 |
| 11 | R.M. N° 864/2019 Protocolo de Prevención, Actuación y Denuncia en Casos de Vio | `normativa_especifica/ne06_rm_864_2019_protocolo_violencia.json` | 6 de 33 | 15 |
| 12 | R.M. N° 069/2025 Reglamento para el Fortalecimiento de la Educación Inclusiva  | `normativa_especifica/ne07_rm_069_2025_educacion_inclusiva.json` | 6 de 33 | 96 |
| 13 | R.M. N° 0020, 0021 y 0022/2024 y modificatoria R.M. N° 534/2025 Reglamento de  | `normativa_especifica/ne14_rm_0020_0021_0022_2024_apertura_modificacion_cierre_regular.json` | 3 de 33 | 0 |
| 14 | R.M. N° 0190/2024 Reglamento de Evaluación del Desarrollo Curricular del Subsi | `normativa_especifica/ne33_rm_0190_2024_evaluacion_desarrollo_curricular_regular.json` | 1 de 33 | 0 |
| 15 | R.M. N° 800/2015 Reglamento de Procedimientos para la Emisión de Libretas de C | `normativa_especifica/ne34_rm_800_2015_libretas_calificaciones_electronicas.json` | 1 de 33 | 0 |
| 16 | R.M. N° 001/2026 del Subsistema de Educación Regular | `normativa_especifica/ne16_rm_001_2026_subsistema_educacion_regular.json` | 3 de 33 | 0 |

Total reutilizado: 490 preguntas.

Además se reutilizaron 9 preguntas del Código Penal (Ley 1768) y 3 del D.S. 1320, que son bibliografía del Asesor Legal.
Nota: la R.M. 001/2026 tiene una versión por subsistema (Regular, Alternativa y Especial, Superior de Formación Profesional); tu lista traía la del Subsistema Regular.

## Cómo cargar tus preguntas
1. Busca el archivo de la norma o libro (por área y nombre) y agrega tus preguntas dentro de `"preguntas": [ ... ]` (modelo en `docs/FORMATO-PREGUNTAS.md`).
2. Valida: `python3 tools/validar_bancos.py` (usa `--todos` para listar cada archivo).
3. Recarga la app: los contadores y los simulacros se actualizan solos.

La app también avisa en pantalla si un JSON tiene errores.

## Agregar o cambiar bibliografías
1. Edita `data/config.json`: `"bibliografias"` (la norma o libro) y `"bibs"` de los cargos que la rinden.
2. Ejecuta `python3 tools/sync_bancos.py`: crea el archivo que falte y actualiza las cabeceras sin tocar tus preguntas.

## Examen (valores referenciales)
La convocatoria no publica el nº de preguntas, el tiempo ni la nota mínima: los definirá el Reglamento (R.M.).
Hoy: 100 preguntas · 120 min · aprobación 60% · 30% normativa general + 40% normativa específica + 30% técnico pedagógico,
repartidas de forma pareja entre las bibliografías del cargo que tengan preguntas (si un área está vacía, las demás cubren su parte).
Se ajusta en `data/config.json` → `perfiles.general`.

Los cargos «Catedrático de Lengua Originaria, Área Productiva, Apoyo/Intérprete y Bienestar Estudiantil» no tienen sección propia en la Bibliografía V4: usan la lista de «Catedrático Docente» (referencial).
La convocatoria agrupa Unidad Educativa, CEA y CEE en un solo cargo; la Bibliografía V4 los separa, por eso la app los muestra como tres cargos.

## Ejecutar en local
```
python3 -m http.server 8000      # en esta carpeta
```
Abre http://localhost:8000 (no abras los HTML con doble clic: el navegador bloquea la lectura de los JSON).
La contraseña de acceso está en `assets/js/pages/login.js` (constante `PASSWORD`).

## Publicar
Sube la carpeta completa a GitHub Pages, Netlify o cualquier hosting estático (mantén `data/` junto a los HTML).
