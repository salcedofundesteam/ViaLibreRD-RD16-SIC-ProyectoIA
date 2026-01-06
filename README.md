# Via Libre RD: Sistema Inteligente de Gestión de Tráfico

**Optimizando la Movilidad Dominicana mediante Visión Artificial y Análisis Predictivo**

Sistema de monitoreo y optimización de flujo vehicular y peatonal que utiliza inteligencia artificial para mejorar la movilidad urbana en República Dominicana.

---

## Tabla de Contenidos

- [Abstract](#abstract)
    - [Objetivos del Proyecto](#objetivos-del-proyecto)
    - [Arquitectura del Sistema](#arquitectura-del-sistema)
    - [Fuentes de Datos](#fuentes-de-datos)
    - [Imagnes de referencia](#imagenes-de-referencia)
    - [Decisiones de Diseño](#decisiones-de-diseño)
    - [Resultados y Conclusión](#resultados-y-conclusión)
- [Stack Tecnológico](#stack-tecnológico)

---

## Abstract

Via Libre RD implementa un sistema de visión por computadora diseñado específicamente para analizar y optimizar el flujo de tráfico en las intersecciones urbanas de República Dominicana. Utilizando algoritmos de detección de objetos en tiempo real, el sistema monitorea vehículos y peatones, cuantifica patrones de movilidad y genera insights para la toma de decisiones en gestión de tráfico.

Este proyecto aborda los desafíos únicos de movilidad en entornos urbanos dominicanos, donde la alta densidad vehicular, la diversidad de tipos de vehículos y los patrones de comportamiento peatonal requieren soluciones adaptativas. Al implementar un sistema basado en datos en tiempo real, buscamos reducir los tiempos de congestión, mejorar la seguridad vial y proporcionar a las autoridades herramientas objetivas para la planificación urbana.

La solución combina técnicas tradicionales de visión por computadora con un enfoque pragmático hacia las condiciones locales, transformando flujos de video en métricas accionables que reflejan la realidad del tráfico dominicano.

---

## Objetivos del Proyecto

### I. Monitoreo en Tiempo Real
Implementar un sistema de detección que funcione en condiciones locales diversas, adaptándose a las particularidades del parque vehicular y comportamiento peatonal dominicano.

### II. Análisis de Patrones de Congestión
Identificar puntos críticos de congestión y patrones horarios específicos del contexto dominicano, considerando factores como horarios laborales, eventos especiales y condiciones climáticas locales.

### III. Generación de Reportes Contextualizados
Desarrollar visualizaciones y reportes que comuniquen efectivamente las métricas de tráfico a tomadores de decisiones municipales y autoridades de tránsito.

### IV. Validación con Datos Locales
Utilizar material de video representativo de entornos urbanos dominicanos para entrenar y validar el sistema, asegurando su relevancia y efectividad en el contexto local.

### V. Diseño para Escalabilidad
Crear una arquitectura modular que pueda extenderse de intersecciones individuales a redes de tráfico completas, con potencial integración futura con sistemas de semaforización inteligente.

El proyecto está dirigido a autoridades municipales, el Instituto Nacional de Tránsito y Transporte Terrestre (INTRANT), y planificadores urbanos que buscan implementar soluciones de ciudad inteligente basadas en evidencia empírica local.

---


<details>
  <summary><h1> Arquitectura del Sistema</h1></summary>



### Módulo de Detección (detectors.py)
Implementa clasificadores Haar Cascade optimizados para las condiciones visuales locales. Incluye ajustes específicos para:
- Diversidad de vehículos (motocicletas, carros públicos, camiones)
- Condiciones de iluminación tropical
- Comportamiento peatonal en entornos urbanos dominicanos

### Módulo de Gestión de Datos (data_manager.py)
Estructura las métricas recopiladas en formatos estandarizados para análisis comparativo:
- Conteos por tipo de vehículo
- Densidad por hora y día de la semana
- Identificación de picos de congestión
- Exportación en formatos compatibles con herramientas de análisis dominicanas

### Módulo de Configuración (config.py)
Centraliza parámetros ajustables al contexto local:
- Definición de horarios pico según patrones laborales dominicanos
- Umbrales de congestión basados en estándares locales
- Configuraciones para condiciones climáticas tropicales

### Módulo de Visualización (visualizar_datos.py)
Genera reportes y gráficos adaptados a las necesidades de reporteo institucional local, incluyendo:
- Gráficas de congestión por corredor vial
- Reportes horarios para turnos de agentes de tránsito
- Visualizaciones para presentaciones públicas

### Entrada Principal (main.py)
Sistema principal que coordina la captura, procesamiento y visualización, diseñado para ejecución en hardware accesible localmente.

</details>

<br>

## Fuentes de Datos

### Datos Generados por el Sistema
- **Videos de prueba**: Material grabado en entornos urbanos dominicanos que representan escenarios realistas
- **Datos de detección**: CSV estructurado con clasificaciones relevantes al parque vehicular local
- **Métricas contextualizadas**: Estadísticas que consideran particularidades del tráfico dominicano

### Modelos Preentrenados y Ajustados
- **Clasificador para vehículos**: Ajustado para reconocer la diversidad del parque vehicular dominicano
- **Clasificador para peatones**: Optimizado para detección en condiciones de alta densidad peatonal
- **Modelos complementarios**: Para posibles extensiones (ej. detección de infracciones comunes)

### Datos de Referencia Local
- **Patrones horarios**: Basados en estudios de movilidad urbana en ciudades dominicanas
- **Umbrales de servicio**: Definidos según criterios del INTRANT y mejores prácticas locales

### Estructura de Datos de Salida

_Estructura sujerida de output_
Cada detección incluye contexto local relevante:
```csv
timestamp,tipo_vehiculo,x,y,ancho,alto,confianza,frame,corredor_vial
2023-10-15 07:45:22,carro,320,240,50,30,0.82,1250
2023-10-15 07:45:22,motocicleta,150,400,20,40,0.75,1250,Av.27deFebrero
2023-10-15 07:45:22,peatón,280,380,15,50,0.88,1250,Av.27deFebrero

```

---


### Imagenes de referencia: 


- _[Imagen de Referencia 1](/img/imagenDereferencia1.png)_
- _[Imagen de Referencia 2](/img/ImagenDeReferenca2.jpg)_
- _[Imagen de Referencia 3](/img/ImagenDeReferenca3.jpg)_
  


## Decisiones de Diseño

### 1. Selección de Algoritmos Balanceada
Optamos por Haar Cascade considerando:
- **Compatibilidad con hardware accesible**: Funciona en equipos de gama media
- **Balance precisión-rendimiento**: Adecuado para monitoreo continuo
- **Facilidad de ajuste**: Permite optimización para condiciones locales

### 2. Arquitectura Modular y Extensible
Diseñamos el sistema para:
- **Adaptación regional**: Módulos configurables por ciudad o municipio
- **Integración progresiva**: Compatible con sistemas existentes
- **Mantenimiento local**: Documentación clara para técnicos locales


### 4. Priorización de Usabilidad
Interfaz diseñada para:
- **Operadores no técnicos**: Visualizaciones intuitivas y controles sencillos
- **Contexto institucional**: Reportes en formatos familiares para autoridades
- **Multiturno**: Persistencia de datos entre sesiones y turnos

---

## Resultados y Conclusión

### Hallazgos Iniciales
El sistema demuestra capacidad para:
1. Monitorear flujos vehiculares diversos con precisión adaptada al contexto local
2. Identificar patrones de congestión específicos de horarios y ubicaciones dominicanas
3. Generar reportes útiles para la toma de decisiones municipales

### Impacto Potencial en RD
- **Mejora en planificación urbana**: Datos objetivos para decisiones de infraestructura
- **Optimización de recursos**: Asignación eficiente de agentes de tránsito según necesidades reales
- **Base para semaforización inteligente**: Datos para futuros sistemas adaptativos
- **Transparencia en gestión de tráfico**: Métricas objetivas para evaluación de políticas

### Limitaciones y Trabajo Futuro
**Limitaciones Actuales**:
- Dependencia de ángulos de cámara específicos
- Precisión variable en condiciones climáticas extremas
- Necesidad de calibración por ubicación

<br>

**Mejoras Planeadas**:
1. Modelos específicos para vehículos comunes en RD (motoconchos, carros públicos)
2. Integración con datos de Waze o aplicaciones de tráfico locales
3. Análisis de puntos de conflicto vehículo-peatón en cruces críticos
4. Versión para dispositivos móviles para monitoreo temporal
5. Dashboard web para acceso remoto de autoridades municipales

### Conclusión
Via Libre RD representa una solución práctica y escalable para los desafíos de movilidad urbana en República Dominicana. Al proporcionar herramientas de monitoreo objetivo y análisis de datos, empodera a las autoridades locales para tomar decisiones basadas en evidencia rather than intuición.

El enfoque en adaptación local, usabilidad institucional y escalabilidad progresiva posiciona este sistema como una base sólida para el desarrollo de ciudades inteligentes en el contexto dominicano.

---


## Stack Tecnológico

### Framework Principal
| Tecnología | Propósito | Justificación para Contexto RD |
|------------|-----------|-------------------------------|
| Python 3.8+ | Lenguaje principal | Amplia comunidad local, recursos educativos disponibles |
| OpenCV 4.5+ | Procesamiento de video | Estándar industrial, buena documentación en español |

### Procesamiento de Datos
| Tecnología | Propósito | Justificación para Contexto RD |
|------------|-----------|-------------------------------|
| Pandas | Análisis de datos | Compatible con herramientas de análisis usadas localmente |
| CSV/Excel | Exportación de datos | Formatos familiares para instituciones dominicanas |

### Visualización
| Tecnología | Propósito | Justificación para Contexto RD |
|------------|-----------|-------------------------------|
| Matplotlib | Gráficos estáticos | Bajo requerimiento de recursos, fácil generación de reportes |
| OpenCV | Visualización en tiempo real | Rendimiento en hardware modesto |

### Recursos Técnicos
- **OpenCV Community**: Por las bibliotecas de visión por computadora
- **Python Dominicana**: Por la comunidad local de soporte técnico

### Inspiración y Contexto
- **Iniciativas de movilidad urbana** en ciudades latinoamericanas con desafíos similares
- **Necesidad de soluciones prácticas** que balanceen tecnología avanzada y factibilidad local
- **Compromiso con la mejora continua** de la calidad de vida urbana en RD

### Notas para Contribuciones
Este proyecto está abierto a mejoras que consideren el contexto dominicano. Priorizamos:
1. Adaptaciones a condiciones locales específicas
2. Optimizaciones para hardware disponible en el mercado local
3. Integraciones con sistemas institucionales existentes
4. Documentación en español claro y accesible

---

**Via Libre RD** - Monitoreo inteligente para una movilidad más fluida y segura en República Dominicana.

_Sistema desarrollado con enfoque en la realidad dominicana, para autoridades dominicanas, con tecnología al servicio del desarrollo urbano sostenible._