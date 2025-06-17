CREATE TABLE keys (
	id SERIAL NOT NULL, 
	key VARCHAR NOT NULL, 
	is_criterion BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (key)
);

CREATE TABLE languages (
	language_id SERIAL NOT NULL, 
	name VARCHAR, 
	PRIMARY KEY (language_id)
);

CREATE TABLE questions (
	question_id SERIAL NOT NULL, 
	text TEXT NOT NULL, 
	PRIMARY KEY (question_id)
);

CREATE TABLE teams (
	team_id SERIAL NOT NULL, 
	team_name VARCHAR, 
	lead_id INTEGER, 
	PRIMARY KEY (team_id), 
	CONSTRAINT fk_team_lead FOREIGN KEY(lead_id) REFERENCES users (user_id)
);

CREATE TABLE users (
	user_id SERIAL NOT NULL, 
	name VARCHAR, 
	email VARCHAR, 
	role VARCHAR, 
	team_id INTEGER, 
	PRIMARY KEY (user_id), 
	FOREIGN KEY(team_id) REFERENCES teams (team_id)
);

CREATE TABLE frameworks (
	framework_id SERIAL NOT NULL, 
	name VARCHAR, 
	language_id INTEGER, 
	feasibility FLOAT, 
	novelty FLOAT, 
	usefulness FLOAT, 
	PRIMARY KEY (framework_id), 
	FOREIGN KEY(language_id) REFERENCES languages (language_id)
);

CREATE TABLE options (
	option_id SERIAL NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	image_path VARCHAR, 
	key VARCHAR NOT NULL, 
	question_id INTEGER NOT NULL, 
	next_question_id INTEGER, 
	PRIMARY KEY (option_id), 
	FOREIGN KEY(question_id) REFERENCES questions (question_id), 
	FOREIGN KEY(next_question_id) REFERENCES questions (question_id)
);

CREATE TABLE question_keys (
	id SERIAL NOT NULL, 
	question_id INTEGER NOT NULL, 
	key_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(question_id) REFERENCES questions (question_id), 
	FOREIGN KEY(key_id) REFERENCES keys (id)
);

CREATE TABLE results (
	id SERIAL NOT NULL, 
	user_id INTEGER NOT NULL, 
	query_keys JSONB NOT NULL, 
	smart_results JSONB, 
	ahp_results JSONB, 
	adaptive_weighted_results JSONB, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (user_id)
);

CREATE TABLE developers (
	developer_id SERIAL NOT NULL, 
	name VARCHAR, 
	technology_id INTEGER, 
	framework_id INTEGER, 
	team_id INTEGER, 
	PRIMARY KEY (developer_id), 
	FOREIGN KEY(technology_id) REFERENCES languages (language_id), 
	FOREIGN KEY(framework_id) REFERENCES frameworks (framework_id), 
	FOREIGN KEY(team_id) REFERENCES teams (team_id)
);

CREATE TABLE frameworks_keys (
	framework_id INTEGER NOT NULL, 
	key_id INTEGER NOT NULL, 
	smart_score FLOAT, 
	ahp_score FLOAT, 
	PRIMARY KEY (framework_id, key_id), 
	FOREIGN KEY(framework_id) REFERENCES frameworks (framework_id), 
	FOREIGN KEY(key_id) REFERENCES keys (id)
);
