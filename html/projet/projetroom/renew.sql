
CREATE DATABASE renew;
CREATE table clients (
    id_client int AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    email VARCHAR(255),
    mdp VARCHAR(255),
    PRIMARY KEY(id_client)
)
CREATE table vetement(
    id_vetement int AUTO_INCREMENT,
    id_client int,
    categorie VARCHAR(255),
    matiere VARCHAR(255),
    taille VARCHAR(255),
    etat VARCHAR(255),
    note VARCHAR(255),
    PRIMARY KEY(id_vetement),
    FOREIGN KEY (id_client) REFERENCES clients(id_client)
);