create table personal_info(
cedula int primary key,
nombre varchar(100) not null,
ocupacion varchar(100) not null
);

create table person (
    rut int primary key,                      -- rut único de la persona
    laboral_income int not null,             -- ingreso laboral
    other_income int not null,               -- otros ingresos
    withholding_source int not null,         -- retención de fuente
    social_security_payments int not null,   -- pagos de seguridad social
    pension_contributions int not null,      -- aportes a pensión
    mortgage_payments int null,         -- pagos por crédito hipotecario
    donations int null,                  -- donaciones
    educational_expenses int null,       -- gastos de educación
    cedula int,                              -- referencia al `cedula` en `personal_info`
    foreign key (cedula) references personal_info(cedula)  -- relación con `personal_info`
);

create table income_declaration (
    id int primary key,         -- id único de la declaración de ingresos
    rut int,                    -- rut de la persona (clave foránea)
    total_ingresos_gravados int,   -- ingresos gravados
    total_ingresos_no_gravados int, -- ingresos no gravados (deducciones)
    total_costos_deducibles int,    -- costos deducibles
    valor_impuesto int,         -- valor del impuesto a pagar
    foreign key (rut) references person(rut)  -- relación con `person`
);