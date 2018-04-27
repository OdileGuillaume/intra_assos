DROP TABLE IF EXISTS usr         CASCADE;
DROP TABLE IF EXISTS association CASCADE;
DROP TABLE IF EXISTS meetings    CASCADE;
DROP TABLE IF EXISTS usr_asso    CASCADE;

CREATE TABLE usr_asso (
  id              SERIAL        NOT NULL,
  usr_name        VARCHAR(64)   NOT NULL,
  asso_name       VARCHAR(64)   NOT NULL,
  status          INT           NOT NULL,

  UNIQUE (usr_name, asso_name),
  PRIMARY KEY (id)
);

CREATE TABLE usr (
  id              SERIAL        NOT NULL,
  e_mail          VARCHAR(64)   NOT NULL,
  password        VARCHAR(64)   NOT NULL,
  status          INT           NOT NULL,
  picture         VARCHAR(256)  NOT NULL,
  asso            VARCHAR(64)   REFERENCES usr_asso(asso_name),

  PRIMARY KEY (e_mail)
);

CREATE TABLE association (
  id              SERIAL        NOT NULL,
  name            VARCHAR(64)   NOT NULL,
  e_mail          VARCHAR(64)   NOT NULL,
  website         VARCHAR(256)          ,
  president       VARCHAR(64)   REFERENCES usr_asso(usr_name) NOT NULL,

  PRIMARY KEY (name)
);


CREATE TABLE meetings (
  id              SERIAL        NOT NULL,
  schedule        TIMESTAMP     NOT NULL,
  place           VARCHAR (256) NOT NULL,
  private         BOOLEAN       NOT NULL,

  PRIMARY KEY (id)
);
