CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;

CREATE TABLE IF NOT EXISTS customers (
    id BIGSERIAL PRIMARY KEY,

    national_code VARCHAR(20),
    account_number TEXT,
    full_name TEXT,
    father_name TEXT,
    id_number VARCHAR(20),
    birth_date DATE,
    age INT,

    city_name TEXT,
    province_name TEXT,
    birth_city TEXT,
    birth_province TEXT,
    address TEXT,

    card_no VARCHAR(30),
    mobile VARCHAR(20),

    gender TEXT,

    source TEXT,
    imported_at TIMESTAMP DEFAULT NOW()
);

-- Exact match
CREATE INDEX idx_national_code ON customers(national_code);
CREATE INDEX idx_account_number ON customers USING GIN (account_number gin_trgm_ops);
CREATE INDEX idx_mobile ON customers(mobile);
CREATE INDEX idx_card_no ON customers(card_no);

-- Text search
CREATE INDEX idx_full_name_gin ON customers USING GIN (to_tsvector('simple', unaccent(full_name)));
CREATE INDEX idx_father_name_gin ON customers USING GIN (to_tsvector('simple', unaccent(father_name)));

-- Filters
CREATE INDEX idx_birth_date_brin ON customers USING BRIN (birth_date);
CREATE INDEX idx_age ON customers(age);
CREATE INDEX idx_gender ON customers(gender);
CREATE INDEX idx_city_name ON customers(city_name);
CREATE INDEX idx_province_name ON customers(province_name);
CREATE INDEX idx_birth_city ON customers(birth_city);
CREATE INDEX idx_birth_province ON customers(birth_province);
