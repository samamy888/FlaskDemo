CREATE DATABASE bleswplandb;
CREATE TABLE bleswplandb.dblist (
    Id INT auto_increment NOT NULL,
	IP varchar(100) NOT NULL,
	Port INT NOT NULL,
	Account varchar(100) NOT NULL,
	Password varchar(100) NOT NULL,
	Status INT DEFAULT 0 NOT NULL,
	CONSTRAINT dblist_pk PRIMARY KEY (Id)
)

INSERT INTO bleswplandb.dblist (IP,Port,Account,Password,Status) VALUES
	 ('localhost',3306,'root','123456',-1),
	 ('localhost',3307,'root','123456',1);

