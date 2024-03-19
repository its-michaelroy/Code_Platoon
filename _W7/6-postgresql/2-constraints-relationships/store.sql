-- Drop the table if it exists

-- Insert Sample Data into Game Table
-- \COPY game FROM './data/game.csv' WITH CSV HEADER;


DROP TABLE IF EXISTS action_figure;

CREATE TABLE action_figure (
    id INT PRIMARY KEY,
    action_figure_title VARCHAR(30)
        NOT NULL
        UNIQUE
        CHECK (action_figure_title ~ '^[A-Z][A-Za-z\-]*([A-Z0-9][a-z]*)*$'),
    quantity INT
        NOT NULL
        CHECK (quantity BETWEEN 1 AND 30),
    price DECIMAL(5,2)
        NOT NULL
        CHECK(price BETWEEN 10 AND 100)
);

\COPY action_figure FROM './data/action_figure.csv' WITH CSV HEADER;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL CHECK (employee_name ~ '^[A-Za-z ]+$'),
    position VARCHAR(255) NOT NULL CHECK (position IN (
        'Sales Associate',
        'Store Manager',
        'Inventory Clerk',
        'Customer Service Representative',
        'IT Specialist',
        'Marketing Coordinator',
        'Assistant Manager',
        'Finance Analyst',
        'Security Officer',
        'HR Coordinator')),
    salary DECIMAL(7,2) CHECK (salary BETWEEN 16.66 AND 31.25)
);

\COPY employee FROM './data/employee.csv' WITH CSV HEADER;

DROP TABLE IF EXISTS poster;

CREATE TABLE poster (
    id INT PRIMARY KEY,
    poster_title VARCHAR(255) NOT NULL UNIQUE CHECK (poster_title ~ '^[A-Za-z0-9- ]+$'),
    quantity INT CHECK (quantity BETWEEN 1 AND 30),
    price DECIMAL(4,2) CHECK (price BETWEEN 6 AND 20)
);

\COPY poster FROM './data/poster.csv' WITH CSV HEADER;

DROP TABLE IF EXISTS game;

-- Create Game Table
CREATE TABLE game (
    game_id SERIAL PRIMARY KEY,
    game_title VARCHAR(255)
        UNIQUE
        NOT NULL
        CHECK (game_title ~ '^[A-Z][A-Za-z0-9 _\-:''\\]+$'),
    quantity INT
        NOT NULL
        CHECK(quantity > 0),
    price DECIMAL(4, 2)
        NOT NULL
        CHECK(price > 10 AND price < 60)
);
