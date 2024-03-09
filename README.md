# Ejercicio del Bootcamp de Ciencias de la Computación - Tokenizer
## _Tokenizer_

## fiso language

### Tipos de Tokens
- **INT**: 123, 78, 8, 9
- **FLOAT**: 4.5, 89.23
- **VAR**: 'mi_var', 'a', 'x_1'
- **OP**: +, -, *, /
- **ASSIGN**: =

### Programa de ejemplo (archivo program.txt)
```sh
5 + 3
44 / 22
1766 - 89
mi_var = 5.4
a = 11 + 2 * 3
z1 = x_1 + y_1
```

### Prueba
```sh
py tokenizer.py program.txt
```

### Salida
Cada token tiene una representación así: <type, value, line, column>

```sh
[
<INT, 5, 0, 0>,
<OP, +, 0, 2>,
<INT, 3, 0, 4>,
<INT, 44, 1, 0>,
<OP, /, 1, 3>,
<INT, 22, 1, 5>,
<INT, 1766, 2, 0>,
<OP, -, 2, 5>,
<INT, 89, 2, 7>,
<VAR, mi_var, 3, 0>,
<ASSIGN, =, 3, 7>,
<FLOAT, 5.4, 3, 9>,
<VAR, a, 4, 0>,
<ASSIGN, =, 4, 2>,
<INT, 11, 4, 4>,
<OP, +, 4, 7>,
<INT, 2, 4, 9>,
<OP, *, 4, 11>,
<INT, 3, 4, 13>,
<VAR, z1, 5, 0>,
<ASSIGN, =, 5, 3>,
<VAR, x_1, 5, 5>,
<OP, +, 5, 9>,
<VAR, y_1, 5, 11>
]
```