create table income_declaration (
    id serial primary key,         -- id único de la declaración de ingresos
    rut int UNIQUE,                    -- rut de la persona (clave foránea)
    total_ingresos_gravados bigint,   -- ingresos gravados
    total_ingresos_no_gravados bigint, -- ingresos no gravados (deducciones)
    total_costos_deducibles bigint,    -- costos deducibles
    valor_impuesto bigint,         -- valor del impuesto a pagar
    foreign key (rut) references natural_person(rut) ON DELETE CASCADE -- relación con `person`
);