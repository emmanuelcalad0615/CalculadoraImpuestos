# Proyecto Calculadora de Impuestos

## Descripción del Proyecto

Este proyecto es una Calculadora de Impuestos que calcula el monto del impuesto a pagar basado en diversos parámetros de ingresos y gastos. Valida los valores de entrada para asegurar que sean positivos y cumplan con condiciones específicas antes de realizar el cálculo del impuesto.

## Autores

- Mario Andrade Rojas
-Samuel Villa Carmona

## Estructura del Proyecto
### Carpetas Principales:
#### GUI/

##### Calculadora_gui.py: 
Archivo principal de la interfaz gráfica del usuario (GUI). Permite la interacción visual con el usuario para ingresar datos y mostrar resultados.

#### src/Console/

##### Calculadora_Console.py: 
Archivo encargado de la interacción en consola. Solicita al usuario sus ingresos y gastos y calcula los impuestos basados en los valores introducidos.

#### src/Logi/
##### Calculadora.py:
 Contiene la lógica principal de cálculo de impuestos, con las fórmulas y reglas necesarias.


#### test/

##### Calculadora_tests.py: 
Archivo que contiene las pruebas unitarias de los cálculos de impuestos. Verifica el correcto funcionamiento de las fórmulas y lógicas definidas.
##### Casos_Calculadora.py: 
Incluye diferentes casos de prueba, como casos normales, extraordinarios y de error, para verificar el comportamiento del sistema.
##### Exceptions.py: 
Define las excepciones personalizadas utilizadas en el sistema para gestionar errores relacionados con los datos introducidos.


## Como ejectutar?

### Interfaz de Consola: 

-Navega a la carpeta src/Console y ejecuta el archivo Calculadora_Console.py:
 ##### python src/Console/Calculadora_Console.py

-Al ejecutar el programa, se te solicitarán tus ingresos y gastos mensuales. Introduce los valores numéricos sin comas, espacios ni caracteres especiales (ej. #$%&+-). El programa validará los datos y, si todo es correcto, calculará el monto del impuesto que deberías pagar.

### Interfaz Grafica: 

La carpeta GUI contiene la implementación de la interfaz gráfica del proyecto. El archivo principal es Calculadora_gui.py, donde se encuentran los elementos visuales que permiten al usuario interactuar con la calculadora de una manera más intuitiva y amigable.

Este archivo utiliza bibliotecas gráficas de Kivy para crear la ventana, botones y campos de entrada necesarios para ingresar los datos del usuario (ingresos y gastos), y muestra el resultado del cálculo en pantalla.

#### Desde consola: 

Para abrir la interfaz gráfica desde la consola, sigue estos pasos:

-Navega a la carpeta raíz del proyecto (CalculadoraImpuestos).

-Ejecuta el archivo Calculadora_gui.py desde la consola:
##### python GUI/Calculadora_gui.py

Esto abrirá la interfaz gráfica de la calculadora, donde podrás ingresar tus ingresos y gastos de manera interactiva.

