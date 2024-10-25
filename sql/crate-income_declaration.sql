CREATE TABLE income_declaration (
    id SERIAL PRIMARY KEY,                        -- unique ID for the income declaration
    rut INT UNIQUE,                               -- RUT of the person (foreign key)
    total_taxable_income BIGINT,                 -- taxable income
    total_non_taxable_income BIGINT,             -- non-taxable income (deductions)
    total_deductible_costs BIGINT,               -- deductible costs
    tax_value BIGINT,                            -- tax amount to be paid
    FOREIGN KEY (rut) REFERENCES natural_person(rut) ON DELETE CASCADE -- relationship with `natural_person`
);