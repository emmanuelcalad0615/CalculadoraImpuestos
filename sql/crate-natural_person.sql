create table natural_person (
    rut int primary key,                      -- rut único de la persona
    laboral_income bigint not null,             -- ingreso laboral
    other_income bigint not null,               -- otros ingresos
    withholding_source bigint not null,         -- retención de fuente
    social_security_payments bigint not null,   -- pagos de seguridad social
    pension_contributions bigint not null,      -- aportes a pensión
    mortgage_payments bigint null,         -- pagos por crédito hipotecario
    donations bigint null,                  -- donaciones
    educational_expenses bigint null,       -- gastos de educación
    cedula bigint,                              -- referencia al `cedula` en `personal_info`
    foreign key (cedula) references personal_info(cedula) ON DELETE CASCADE -- relación con `personal_info`
);