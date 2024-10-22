create table natural_person (
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