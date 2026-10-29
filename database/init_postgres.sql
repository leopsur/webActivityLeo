CREATE TABLE IF NOT EXISTS profesores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL
);

INSERT INTO profesores (nombre, especialidad, departamento) VALUES
('Dra. Elena Beltrán', 'Inteligencia Artificial', 'Informática'),
('Prof. Javier Gómez', 'Matemáticas Aplicadas', 'Ciencias Exactas'),
('Dra. Carmen Ruiz', 'Literatura Hispánica', 'Lengua y Literatura');