import sqlite3 as sql3

con = sql3.connect("./data.db")
cur = con.cursor()
req = "create table if not exists User (id int AUTO_INCREMENT primary key, username varchar(32), email varchar(32), password varchar(256), phone int)"
cur.execute(req)
req = "create table if not exists fournisseur(id int AUTO_INCREMENT primary key, Nom varchar(32), email varchar(32), telephone int )"
cur.execute(req)
req = "create table if not exists categorie(id int AUTO_INCREMENT primary key, intitule varchar(32), Budget int, Depense int, Budget_Actuelle int)"
cur.execute(req)
req = "create table if not exists article(id int AUTO_INCREMENT primary key, code varchar(10) unique, Nom varchar(32), stock int default 0, categorie int, fournisseur int, foreign key(categorie) references categorie(id),foreign key(fournisseur) references fournisseur(id) )"
cur.execute(req)
req = "create table if not exists entree(id int AUTO_INCREMENT primary key, code varchar(10), type varchar(32), date_operation date)"
cur.execute(req)
req = "create table if not exists sortie(id int AUTO_INCREMENT primary key, code varchar(10), type varchar(32), date_operation date)"
cur.execute(req)
req = "create table if not exists cout(id int AUTO_INCREMENT primary key, code varchar(10), operation varchar(32), montant int, article int,foreign key(article) references article(article))"
cur.execute(req)
req = "create table if not exists article_sortie (id int AUTO_INCREMENT primary key, quantite int, article int, sortie int, foreign key(article) references article (article),foreign key(sortie) references sortie(sortie))"
cur.execute(req)
req = "create table if not exists article_entree (id int AUTO_INCREMENT primary key, quantite int, article int, entree int, foreign key(article) references article(article),foreign key(entree) references entree(entree))"
cur.execute(req)
