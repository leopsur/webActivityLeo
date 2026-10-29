CREATE DATABASE IF NOT EXISTS activityleo_mysql;
USE activityleo_mysql;

CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    grado VARCHAR(50) NOT NULL
);

INSERT INTO alumnos (nombre, email, grado) VALUES
('María García', 'maria.garcia@example.com', '3º ESO'),
('Carlos Rodríguez', 'carlos.r@example.com', '1º Bachillerato'),
('Laura Martínez', 'laura.m@example.com', '2º Bachillerato');