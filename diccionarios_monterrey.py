#!/usr/bin/env python
# coding: utf-8

# In[1]:


diccionario_presidente = {
    "obligatorias": [
        "Presidente Municipal", "Alcalde de Monterrey", "Adrián de la Garza", 
        "Adrián Emilio de la Garza Santos", "Edil de Monterrey", "alcalde regio", 
        "alcalde regiomontano", "Edil regiomontano", "Adrián DLG", "Alcalde Adrián"
    ],
    "relevantes": [
        "rinde informe de gobierno", "encabeza el cabildo", "iniciativa", "responde a críticas", 
        "destaca avances en seguridad", "promete inversión"
    ]
}

diccionario_ayuntamiento = {
    "obligatorias": [
        "Secretaría del Ayuntamiento", "Ayuntamiento de Monterrey", "Ayuntamiento municipal",
        "Ayunta miento", "César Garza", "César Garza Villarreal", "César A. Garza", "C. Garza", "Ayuntamiento", "ayuntamiento", "predial"
    ],
    "relevantes": [
        "cabildo", "sesión de cabildo", "sesión ordinaria del cabildo", "sesión extraordinaria del cabildo",
        "reunión del cabildo", "regidores", "síndicos municipales", "reglamentos municipales",
        "reglamento", "modificación al reglamento", "modificaciones al reglamento municipal",
        "aprueba reglamento", "aprueban reformas", "votan en cabildo", "discuten reglamento",
        "autoriza licencias", "autorización de licencias", "cancela permisos", "cancelación de licencias",
        "licencias", "licencia" "licencias de alcohol", "permisos de funcionamiento",
        "licencias de uso de suelo", "permisos comerciales", "otorgan permisos",
        "anuncia cambios en reglamentos", "reforma reglamentaria", "gestiona licencias",
        "solicita reforma al reglamento", "cambio en normativa", "cambios al marco legal local",
        "propuesta de reforma", "normativa local", "administración municipal", "gobierno municipal"
    ]
}




diccionario_secretaria_ejecutiva = {
    "obligatorias": [
        "Secretaría Ejecutiva", "Secretario Ejecutivo", "Oficina Ejecutiva", 
        "Gabriel Ayala", "Gabriel Ayala Salazar", "Gabriel A. Salazar", 
        "Director Ejecutivo de Monterrey"
    ],
    "relevantes": []
}


diccionario_contraloria = {
    "obligatorias": [
        "Contraloría municipal", "Contraloría de Monterrey", 
        "Contraloría General", "Jovita Morín", "Jovita Morín Flores", 
        "Contralora de Monterrey", "Contraloría", "contraloría"
    ],
    "relevantes": [
        "auditoría interna", "auditoría municipal", "revisión financiera", 
        "control interno", "fiscalización", "análisis de cuentas públicas", 
        "irregularidades financieras", "presupuesto bajo vigilancia", 
        "desvío de recursos", "corrupción municipal", "fondo malversado", 
        "control de gasto", "manejo indebido del presupuesto", 
        "rendición de cuentas", "auditorías a dependencias", 
        "examen financiero", "supervisión del gasto"
    ]
}


diccionario_seguridad_institucional = {
    "obligatorias": [
        "Secretaría de Seguridad y Protección Ciudadana", "SSPC Monterrey", 
        "Policía Municipal", "Policía de Monterrey", "Seguridad Municipal", 
        "Protección Ciudadana Monterrey", "Secretaría de Seguridad", "Protección Civil", 
        "Seguridad Pública de Monterrey", "policía de monterrey", "policía municipal", "protección civil"
    ],
    "relevantes": [
        "Guadalupe Sánchez", "Guadalupe Eduardo Sánchez Quiroz", 
        "jefe de policía", "secretario de seguridad", "operativo de seguridad", 
        "patrullajes", "presencia policiaca", "contra el crimen", 
        "acciones de vigilancia", "fuerza pública", "vigilancia ciudadana", 
        "informes de seguridad", "reunión de seguridad", 
        "reducción de delitos", "disminución de robos", 
        "estrategias de seguridad", "programa de patrullaje", 
        "coordinación con policía estatal", "acciones preventivas", 
        "refuerzan seguridad", "monitoreo de zonas conflictivas"
    ]
}

diccionario_indices_inseguridad = {
    "obligatorias": [],
    "relevantes": [
        "presuntos delincuentes", "detenciones", "personas detenidas", 
        "cámaras de vigilancia", "cámaras de seguridad", 
        "prevención de la violencia", "índices de violencia", 
        "aumento de delitos", "crecimiento de la inseguridad", 
        "homicidios", "asesinatos", "robos", "asaltos", 
        "crimen organizado", "violencia en Monterrey", 
        "delitos de alto impacto", "zonas peligrosas", "zonas rojas", 
        "incremento delictivo", "alerta de inseguridad",  "presuntos delincuentes", "cámaras de vigilancia", "cámaras de seguridad", 
        "prevención de la violencia", "índices de violencia", "incremento de delitos", 
        "homicidios", "robos", "delitos de alto impacto", "zonas de alto riesgo", 
        "crimen organizado", "violencia en Monterrey", "robo", "secuestro", "inseguridad", "asalto", "homicidio", "narcotraficante","arma","armas", "sin vida"
    ]
}




diccionario_desarrollo_economico = {
    "obligatorias": [],
    "relevantes": [
        "Secretaría de Desarrollo Económico", "Desarrollo Económico Monterrey", 
        "Secretaría Económica", "Ximena Tamariz", "Ximena Tamariz García", 
        "programas de apoyo a pymes", "reactivación económica", "creación de empleos", 
        "llegada de nuevas empresas", "inversiones", "crecimiento económico", 
        "emprendimiento", "capacitación laboral", "emprendedores", "apoya al sector empresarial", 
        "ferias de empleo", "vínculos con empresarios", "programas de financiamiento", 
        "exportaciones locales", "apoya a micro y pequeñas empresas", "inversiones extranjeras", 
        "desarrollo comercial", "comercio local", "alianza público-privada", "recursos para emprendedores", 
        "industria local", "clústeres empresariales", "reactivación económica", 
        "turismo de negocios", "turismo", "fomenta innovación y tecnología", "proyectos productivos", 
        "subsidios para empresas", "empresarios locales", "generación de empleos", 
        "cámaras empresariales", "apoyo a emprendedores", "indicadores económicos", 
        "economía sustentable", "comerciantes afectados", "sector industrial", "desarrollo económico", "plaza"
    ]
}

diccionario_servicios_publicos = {
    "obligatorias": [],
    "relevantes": [
        "Secretaría de Servicios Públicos", "Servicios Públicos", "serviciios públicos", "áreas verdes"
        "Departamento de Servicios Públicos", "Oficina de Servicios Municipales", "basura","banquetas", "baches", "bache", 
        "Secretaría de Mantenimiento Urbano", "Servicios Municipales", "Mantenimiento Municipal",  
        "servicios básicos", "Servicios Urbanos", "alumbrado público", "recolección de basura", 
        "Mayela Quiroga", "Mayela María De Lourdes Quiroga Tamez", "baches", 
        "rehabilitación de parques y jardines", "mantenimiento de calles", "luminarias", 
        "limpieza urbana", "mantenimiento de áreas verdes", "desazolve", "poda de árboles", 
        "fugas de agua", "postes de luz", "reparación de pavimento", "parques", "cableado", 
        "bacheo", "pintura", "alumbrado público", "banqueta", "fuga"
    ]
}

diccionario_infraestructura_sostenible = {
    "obligatorias": [],
    "relevantes": [
        "Secretaría de Infraestructura Sostenible", "obras públicas", "Infraestructura Municipal", 
       "José Nazario Pineda", "Nazario Pineda", "obras públicas", "construcción de vialidades",
        "mantenimiento vial", "reparación de calles", "rehabilitación de vialidades",
        "infraestructura urbana", "pavimentación", "pavimento hidráulico", "recarpeteo", 
        "obras en colonias", "modernización de vialidades", "construcción de puentes", 
        "pasos a desnivel", "construcción de banquetas", "rehabilitación de banquetas",
        "remodelación de espacios públicos", "mantenimiento de carreteras", "obras en curso",
        "licitación de obra pública", "licitaciones municipales", "presupuesto para infraestructura",
        "inversión en obra pública", "reparación de infraestructura", "obra hidráulica",
        "urbanización", "plan maestro de infraestructura", "plan de infraestructura vial", "licitación"
    ]
}

diccionario_desarrollo_urbano = {
    "obligatorias": [],
    "relevantes": [
        "Secretaría de Desarrollo Urbano Sostenible", "SEDUSO", 
        "Desarrollo Urbano Monterrey", "Movilidad Urbana Monterrey", 
        "planeación urbana", "infraestructura verde", "cambio climático", "calidad del aire",
        "SINTRAM", "ciclovías", "reciclaje", "señalética", "Fernando Gutiérrez", 
        "Fernando Gutiérrez Moreno", "cruces seguros", "intersecciones seguras", 
        "bifurcaciones salvavidas", "semaforización", "movilidad barrial", "ampliación de banquetas", 
        "banquetas", "biciescuela", "mitigación climática", "huertos urbanos", "escuelas de lluvia", 
        "captación pluvial", "ahorro de agua", "reducción de emisiones contaminantes", "reforestación",   
        "energía renovable", "eficiencia energética", "áreas verdes", "programas de educación ambiental", 
        "infraestructura verde", "calidad del aire", "uso de suelo", "parques", "gestión integral de residuos", 
        "puntos verdes", "diseño urbano","semáforos", "regio ruta"
    ],
    "contexto": ["Monterrey"]
}

diccionario_desarrollo_humano = {
    "obligatorias": [],
    "relevantes": [
        "Secretaría de Desarrollo Humano e Igualdad Sustantiva", "Desarrollo Humano Monterrey", 
        "Secretaría de Igualdad Sustantiva", "desarrollo social", "mascotas", "veterinaria", 
        "Desarrollo Humano", "Igualdad Sustantiva", "Secretaría de Igualdad", "SDHIS", "Karina Barrón", 
        "Karina Marlen Barrón Perales", "programas de bienestar", "becas educativas", "deporte","deportes"
        "campañas contra la discriminación", "derechos de las mujeres", "inclusión laboral", 
        "vías deportivas", "vía deportiva", "clínica municipal de la salud", 
        "clínica de la salud municipal", "salud", "vacunación", "campaña de vacunaciones", 
        "rehabilitación de centros comunitarios", "programas de prevención de adicciones", 
        "talleres de inclusión social", "educación", "actividades recreativas", "espacios cero cinco", 
        "biblioteca municipal", "útiles útiles", "bienestar animal", "adopción", "esterilización", 
        "veterinario", "vacunas", "vacunación", "campañas de vacunación", "centros de salud", 
        "servicios de salud", "brigadas de salud", "atención psicológica", "salud dental", 
        "salud integral", "brigadas rosas", "grupos vulnerables", "diabetes", "consultas médicas", 
        "familias en situación de riesgo", "canchas", "áreas deportivas", "ciudad deportiva", 
        "consejo de la niñez", "escrituras", "atención psicológica", "deportes", "canchas", "deportivos", "deportivo", "vacunaciones"
    ],
    "contexto": ["Monterrey", "programas deportivos", "infraestructura deportiva", "eventos comunitarios", "canchas municipales"]
}


diccionario_dif = {
    "obligatorias": [
        "DIF Monterrey", "Sistema DIF Municipal", "DIF ", "Sistema para el Desarrollo Integral de la Familia", 
        "Gabriela Oyervides", "Gaby Oyervides", "Xóchitl Francisca Loredo Salazar", "Xóchitl Loredo"
    ],
    "relevantes": [
        "Sistema de Bienestar Familiar", "DIF Local", "Sistema de Cuidados Monterrey", 
        "Institución de Desarrollo Familiar", "sistema de cuidados", "programas de asistencia social", 
        "atención a la primera infancia", "programas de nutrición infantil", "apoyos a personas vulnerables", 
        "personas en situación de vulnerabilidad", "entrega de cobijas", "guarderías municipales", 
        "centros de cuidado infantil", "guarderías públicas", "centros de bienestar familiar", 
        "atención a adultos mayores", "apoyo a cuidadores", "centros de día para adultos mayores", 
        "programas para la tercera edad", "actividades recreativas para adultos mayores", 
        "espacios de convivencia para adultos mayores", "campañas contra el abuso infantil", 
        "prevención de abuso infantil", "trabajo infantil", "espacios de cuidado infantil", 
        "rehabilitación física", "servicios de rehabilitación física", "apoyo a personas con discapacidad", 
        "campañas contra violencia intrafamiliar", "brigadas médicas", "brigadas de asistencia médica", 
        "apoyos económicos", "entrega de apoyos económicos", "centros de atención comunitaria", 
        "crisis familiares", "red de cuidados", "asistencia alimentaria", "comedores comunitarios", 
        "campañas de abrigo", "programas de cuidado infantil"
    ]
}




diccionario_mujeres_regias = {
    "obligatorias": [
        "Instituto de las Mujeres Regias", "IMMR", "Mujeres Regias", 
        "Wendy Maricela Cordero González", "Wendy Cordero"
    ],
    "relevantes": []
}

diccionario_juventud_regia = {
    "obligatorias": [
        "Instituto de la Juventud Regia", "Juventud Regia Monterrey", 
        "Instituto Municipal de la Juventud", "Injure", "Juventud Regia", 
        "Instituto de la Juventud", "Juventud Monterrey", "Maday Frinee Cantú Cantú", 
        "Maday Cantú", "Prepa Regia", "INJURE", 
    ],
    "relevantes": ["programas para jóvenes", "becas para jóvenes", "empleo juvenil", 
        "talleres para jóvenes", "voluntariado juvenil", "prevención de adicciones", 
        "juventudes", "capacitaciones para jóvenes", "liderazgo juvenil", 
        "políticas públicas juveniles", "jóvenes emprendedores", 
        "concursos juveniles", "participación juvenil", "espacios para jóvenes", 
        "creación de espacios juveniles", "fomento a la juventud", "eventos juveniles", 
        "campañas para jóvenes", "salud mental juvenil", "educación para jóvenes"
    ]
}

diccionario_implanc = {
    "obligatorias": [
        "Instituto Municipal de Planeación Urbana y Convivencia", "IMPLANC Monterrey", 
        "Planeación Urbana Monterrey", "IMPLANC"
    ],
    "relevantes": [
        "Planeación Territorial", "Instituto de Planeación", "Oficina de Planeación Urbana", 
        "Planeación Estratégica Monterrey", "Planeación Urbana", "Edgar Rodolfo Olaiz Ortiz", 
        "Edgar Olaiz", "uso de suelo", "plan de desarrollo urbano", "proyectos estratégicos urbanos", 
        "zonificación", "distritos urbanos", "plan de resiliencia", "regeneración urbana", 
        "revitalización del centro histórico", "plan maestro urbano", "proyectos de desarrollo territorial", 
        "planeación metropolitana", "redensificación urbana", "organización territorial", 
        "ordenamiento territorial", "agenda urbana", "reordenamiento del espacio urbano", 
        "análisis del espacio público", "planes de largo plazo", "plan Monterrey 2040"
    ]
}

diccionario_siga = {
    "obligatorias": [
        "Secretaría de Innovación y Gobierno Abierto", "Gobierno Abierto de Monterrey", 
        "Oficina de Gobierno Abierto", "Gobierno Digital Monterrey", "SIGA", 
        "Innovación y Gobierno Abierto", "Transparencia Monterrey","Transparencia", "Sitio web", "página del municipio" 
        "Federico Vargas", "Federico Vargas Rodríguez", "gobierno abierto", "Gobierno abierto"
    ],
    "relevantes": [
        "servicios digitales municipales", "digitalización de trámites", "trámites digitales", 
        "mejora regulatoria", "gobierno digital", "portales digitales", "apertura gubernamental", 
        "datos abiertos", "plataformas de participación ciudadana", "participación ciudadana digital", 
        "portal de transparencia", "innovación cívica", "mejoras en trámites", "automatización de procesos", 
        "gestión digital", "servicios en línea", "app de gobierno", "tecnología cívica", 
        "ciudadanía digital", "monitoreo ciudadano", "infraestructura digital"
    ]
}


