-- Verifica se o banco de dados já existe
SELECT 'api_graphql_postgres_1' FROM pg_database WHERE datname='api_graphql_postgres_1' LIMIT 1;

-- Se o banco de dados não existir, cria
DO $$ 
BEGIN 
  IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'api_graphql_postgres_1') THEN
    CREATE DATABASE api_graphql_postgres_1;
  END IF;
END $$;

-- Conecta ao banco de dados
\c api_graphql_postgres_1;

-- Criação da tabela de DVD (tbl_dvds)
CREATE TABLE IF NOT EXISTS tbl_dvds (
    id serial PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    director VARCHAR(255),
    release_year INT,
    genre VARCHAR(100)
);

-- Insere 15 DVDs fictícios (Carga inicial)
INSERT INTO tbl_dvds (title, director, release_year, genre)
VALUES
  ('DVD 1', 'Director 1', 2001, 'Genre 1'),
  ('DVD 2', 'Director 2', 2002, 'Genre 2'),
  ('DVD 3', 'Director 3', 2003, 'Genre 3'),
  ('DVD 4', 'Director 4', 2004, 'Genre 4'),
  ('DVD 5', 'Director 5', 2005, 'Genre 5'),
  ('DVD 6', 'Director 6', 2006, 'Genre 6'),
  ('DVD 7', 'Director 7', 2007, 'Genre 7'),
  ('DVD 8', 'Director 8', 2008, 'Genre 8'),
  ('DVD 9', 'Director 9', 2009, 'Genre 9'),
  ('DVD 10', 'Director 10', 2010, 'Genre 10'),
  ('DVD 11', 'Director 11', 2011, 'Genre 11'),
  ('DVD 12', 'Director 12', 2012, 'Genre 12'),
  ('DVD 13', 'Director 13', 2013, 'Genre 13'),
  ('DVD 14', 'Director 14', 2014, 'Genre 14'),
  ('DVD 15', 'Director 15', 2015, 'Genre 15');