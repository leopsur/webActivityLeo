CREATE DATABASE IF NOT EXISTS activityleo_mariadb;
USE activityleo_mariadb;

CREATE TABLE IF NOT EXISTS actividades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    cupo INT NOT NULL
);

INSERT INTO actividades (nombre, categoria, cupo) VALUES
('Taller de Programación Python', 'Tecnología', 25),
('Torneo de Ajedrez', 'Deportes', 16),
('Club de Lectura y Debate', 'Humanidades', 12);