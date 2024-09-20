# Proyecto Calculadora de Impuestos

## Descripción del Proyecto

Este proyecto es una Calculadora de Impuestos que calcula el monto del impuesto a pagar basado en diversos parámetros de ingresos y gastos. Valida los valores de entrada para asegurar que sean positivos y cumplan con condiciones específicas antes de realizar el cálculo del impuesto.

## Autores

- Mario Andrade Rojas
-Samuel Villa Carmona

## Estructura del Proyecto

CalculadoraImpuestos/
│
├── GUI/
│   └── Calculadora_gui.py
│
├── src/
│   └── Console/
│       ├── Calculadora_Console.py
│       └── Calculadora.py
│
├── test/
│   ├── Calculadora_tests.py
│   ├── Casos_Calculadora.py
│   └── Exceptions.py
└── README.md

### src/Console

#### src/Console/Calculadora_Console.py:
Este archivo se encarga de la interfaz de usuario en consola. Permite que el usuario introduzca sus ingresos y gastos, y calcula el impuesto basándose en los valores ingresados. Si se ingresan datos incorrectos, se muestran mensajes de error.

#### src/Console/Calculadora.py:
Este archivo contiene toda la lógica de cálculo de impuestos. Implementa fórmulas y condicionales necesarios para determinar el monto del impuesto a pagar en función de los datos introducidos por el usuario.

### GUI

#### GUI/Calculadora_gui.py:
Este archivo corresponde a la interfaz gráfica del proyecto. Proporciona una interfaz de usuario más visual e interactiva, donde los usuarios pueden ingresar sus ingresos y gastos a través de botones, campos de texto, y posiblemente otras características gráficas. La lógica principal del cálculo de impuestos sigue siendo manejada por el archivo Calculadora.py que se encuentra en src/Console.

En este archivo, se incluyen las importaciones necesarias para interactuar con la lógica del proyecto que está ubicada en otras carpetas. Es crucial asegurarse de que los módulos y archivos se importen correctamente para que la interfaz gráfica funcione.

### test


#### Calculadora_tests.py
Este archivo contiene pruebas unitarias y la lógica de verificación de los cálculos realizados por Calculadora.py.

#### Casos_Calculadora.py
 Contiene casos de prueba reales divididos en casos normales, extraordinarios y casos de error, ejecutando las funciones desde Calculadora_tests.py.

#### Exceptions.py
Define excepciones personalizadas para gestionar errores en el ingreso de datos por parte del usuario.


## Como ejectutar?

### Interfaz de Consola: 

-Navega a la carpeta src/Console y ejecuta el archivo Calculadora_Console.py:
 ##### python src/Console/Calculadora_Console.py

-Al ejecutar el programa, se te solicitarán tus ingresos y gastos mensuales. Introduce los valores numéricos sin comas, espacios ni caracteres especiales (ej. #$%&+-). El programa validará los datos y, si todo es correcto, calculará el monto del impuesto que deberías pagar.

### Interfaz Grafica: 

La carpeta GUI contiene la implementación de la interfaz gráfica del proyecto. El archivo principal es Calculadora_gui.py, donde se encuentran los elementos visuales que permiten al usuario interactuar con la calculadora de una manera más intuitiva y amigable.

Este archivo utiliza bibliotecas gráficas (como Tkinter o cualquier otra biblioteca de interfaz de usuario) para crear la ventana, botones y campos de entrada necesarios para ingresar los datos del usuario (ingresos y gastos), y muestra el resultado del cálculo en pantalla.

#### Desde consola: 

Para abrir la interfaz gráfica desde la consola, sigue estos pasos:

-Navega a la carpeta raíz del proyecto (CalculadoraImpuestos).

-Ejecuta el archivo Calculadora_gui.py desde la consola:
##### python GUI/Calculadora_gui.py

Esto abrirá la interfaz gráfica de la calculadora, donde podrás ingresar tus ingresos y gastos de manera interactiva.

