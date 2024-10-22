create table income_declaration (
    id int primary key,         -- id único de la declaración de ingresos
    rut int,                    -- rut de la persona (clave foránea)
    total_ingresos_gravados bigint,   -- ingresos gravados
    total_ingresos_no_gravados bigint, -- ingresos no gravados (deducciones)
    total_costos_deducibles bigint,    -- costos deducibles
    valor_impuesto int,         -- valor del impuesto a pagar
    foreign key (rut) references person(rut)  -- relación con `person`
);