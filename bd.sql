CREATE DATABASE IF NOT EXISTS Banco;
USE Banco;

CREATE TABLE sucursal(
    id_sucursal VARCHAR(5) PRIMARY KEY,
    Nombre VARCHAR(15)
);

CREATE TABLE usuarios(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(20),
    Apellido VARCHAR(20),
    Curp VARCHAR(18),
    Sexo CHAR(1),
    Email VARCHAR(30),
    Pass VARCHAR(15),
    Sucursal VARCHAR(5),
    FOREIGN KEY (Sucursal) REFERENCES sucursal(id_sucursal)
);