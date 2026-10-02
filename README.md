# Laboratorio 7: Git, código limpio, TDD y SOLID

Práctica de control de versiones y buenas prácticas de programación en Python.

## Contenido

| Archivo | Descripción |
|---|---|
| `laboratorio_7.py` | Archivo inicial para practicar Git (commit, rama y merge). |
| `figuras.py` | Cálculo del área de figuras geométricas, refactorizado con nombres claros, funciones y sin código repetido. |
| `primo.py` | Función `es_primo`, desarrollada con TDD. |
| `test_primo.py` | Pruebas unitarias de `es_primo` (`unittest`). |
| `figuras_solid.py` | Rediseño de las figuras aplicando SRP y OCP. |
| `figura_nueva.py` | Figuras nuevas (`Trapecio` y `Elipse`) agregadas sin modificar el código existente. |

## Cómo ejecutar

```
py figuras.py
py figuras_solid.py
py figura_nueva.py
py -m unittest test_primo -v
```

## Desarrollo por puntos

### 1. Uso básico de Git y GitHub
- Repositorio local con `git init` y primer commit.
- Conexión con GitHub mediante `git remote add origin` y `git push`.
- Rama `nueva-rama` con un cambio, unida a `main` con `git merge`.

### 2. Refactorización y código limpio
- `figuras.py` se escribió primero de forma simple y luego se refactorizó aplicando:
  - **Nombres claros:** `radio`, `base`, `altura`.
  - **Modularidad:** una función por cada área y una función `main`.
  - **Sin redundancia:** base y altura se piden una sola vez.

### 3. Test Driven Development (TDD)
Ciclo seguido para `es_primo`, con un commit en cada etapa:
1. **Rojo:** se escribieron los tests primero y fallaron.
2. **Verde:** se implementó la función hasta que pasaron.
3. **Refactor:** se mejoró la eficiencia revisando divisores solo hasta la raíz cuadrada.

### 4. Principios SOLID
- **SRP (Responsabilidad Única):** cada figura calcula su área, `CalculadoraAreas` calcula y `Presentador` solo muestra resultados.
- **OCP (Abierto/Cerrado):** en `figura_nueva.py` se agregan `Trapecio` y `Elipse` sin modificar `Figura`, `CalculadoraAreas` ni `Presentador`.

## Autor
AndersonMato