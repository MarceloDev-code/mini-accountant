# 💰 MiniContador

MiniContador es una aplicación web sencilla para llevar registro de ingresos y egresos personales o de una pequeña empresa. Fue creada con **Flask** y **SQLAlchemy**, y está pensada como un proyecto de portafolio.

## 🚀 Características

- Registro de ingresos y egresos
- Fecha, monto, descripción y tipo
- Resumen total de ingresos, egresos y saldo actual
- CRUD mínimo con persistencia en SQLite

## 📦 Stack

- Flask
- SQLAlchemy
- HTML + CSS simple
- SQLite

## 🧭 Próximos pasos recomendados

### 1) Mejorar la calidad de datos (prioridad alta)
- Validar montos positivos y tipos permitidos (`ingreso`/`egreso`) en backend.
- Manejar errores de formularios (fechas inválidas, campos vacíos, montos no numéricos).
- Estandarizar formato de moneda y fechas en la UI.

### 2) Completar el CRUD (prioridad alta)
- Agregar edición y eliminación de transacciones.
- Incluir confirmación antes de eliminar.
- Mantener historial ordenado y paginado cuando crezca la data.

### 3) Reportería y filtros (prioridad media)
- Filtro por rango de fechas y por tipo.
- Resumen mensual (ingresos, egresos, saldo).
- Exportar a CSV para análisis externo.

### 4) Seguridad y robustez (prioridad media)
- Activar protección CSRF en formularios.
- Mover `SECRET_KEY` y configuración sensible a variables de entorno.
- Agregar validación de entrada y mensajes de error amigables.

### 5) Preparación para producción (prioridad media)
- Añadir tests básicos (rutas, modelo y lógica de saldo).
- Configurar migraciones con Flask-Migrate.
- Crear pipeline simple de CI (lint + tests) en GitHub Actions.

### 6) Escalamiento funcional (prioridad baja)
- Soporte para categorías (arriendo, sueldos, ventas, etc.).
- Dashboard visual con gráficos de tendencia.
- Gestión multiusuario con autenticación.

> Sugerencia: ejecuta los puntos 1 y 2 primero; son los que más elevan el valor del proyecto para portafolio y uso real.

## ✍️ Autor
Marcelo Carvacho
📧 marcelo.carvacho97@gmail.com
🌍 Concepción, Chile
