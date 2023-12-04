CREATE DATABASE golf;

CREATE TABLE utilisateurs (
    id_ut INT AUTO_INCREMENT,
    prenom VARCHAR(255),
    nom VARCHAR(255),
    email TEXT,

    PRIMARY KEY (id_ut)
);

CREATE TABLE golfeurs(
    id_golf INT AUTO_INCREMENT,
    prenom VARCHAR(255),
    nom VARCHAR(225),
    email TEXT,

    PRIMARY KEY (id_golf)
);

INSERT INTO golfeurs (prenom, nom, email) VALUES ('john', 'LEGEND', 'j.legend@gmail.com');
