-- db/schema.sql

CREATE TABLE keys (
	id SERIAL NOT NULL, 
	title VARCHAR NOT NULL, 
	is_criterion BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (title)
);

CREATE TABLE languages (
	id SERIAL NOT NULL, 
	title VARCHAR, 
	PRIMARY KEY (id)
);

CREATE TABLE questions (
	id SERIAL NOT NULL, 
	title TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE teams (
	id SERIAL NOT NULL, 
	title VARCHAR, 
	lead_id INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT fk_team_lead FOREIGN KEY(lead_id) REFERENCES users (id)
);

CREATE TABLE users (
	id SERIAL NOT NULL, 
	full_name VARCHAR, 
	email VARCHAR, 
	role VARCHAR, 
	team_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(team_id) REFERENCES teams (id)
);

CREATE TABLE frameworks (
	id SERIAL NOT NULL, 
	title VARCHAR, 
	language_id INTEGER, 
	feasibility FLOAT, 
	novelty FLOAT, 
	usefulness FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(language_id) REFERENCES languages (id)
);

CREATE TABLE options (
	id SERIAL NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	image_path VARCHAR, 
	key VARCHAR NOT NULL, 
	question_id INTEGER NOT NULL, 
	next_question_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(question_id) REFERENCES questions (id), 
	FOREIGN KEY(next_question_id) REFERENCES questions (id)
);

CREATE TABLE question_keys (
	id SERIAL NOT NULL, 
	question_id INTEGER NOT NULL, 
	key_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(question_id) REFERENCES questions (id), 
	FOREIGN KEY(key_id) REFERENCES keys (id)
);

CREATE TABLE results (
	id SERIAL NOT NULL, 
	user_id INTEGER NOT NULL, 
	query_keys JSONB NOT NULL, 
	smart_results JSONB, 
	ahp_results JSONB, 
	awm_results JSONB, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE developers (
	id SERIAL NOT NULL, 
	full_name VARCHAR, 
	technology_id INTEGER, 
	framework_id INTEGER, 
	team_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(technology_id) REFERENCES languages (id), 
	FOREIGN KEY(framework_id) REFERENCES frameworks (id), 
	FOREIGN KEY(team_id) REFERENCES teams (id)
);

CREATE TABLE frameworks_keys (
	id SERIAL NOT NULL, 
	framework_id INTEGER NOT NULL, 
	key_id INTEGER NOT NULL, 
	smart_score FLOAT, 
	ahp_score FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(framework_id) REFERENCES frameworks (id), 
	FOREIGN KEY(key_id) REFERENCES keys (id)
);

CREATE TABLE resources (
	id SERIAL NOT NULL, 
	title VARCHAR NOT NULL, 
	language_id INTEGER NOT NULL, 
	framework_id INTEGER NOT NULL, 
	rank INTEGER, 
	total INTEGER, 
	type resourcetype NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(language_id) REFERENCES languages (id), 
	FOREIGN KEY(framework_id) REFERENCES frameworks (id)
);
