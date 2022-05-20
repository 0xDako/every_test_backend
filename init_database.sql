DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS users;

CREATE TABLE tests(
    test_id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    invite_code VARCHAR(10),
    question_count INT
);

CREATE TABLE questions(
    question_id SERIAL PRIMARY KEY,
    test_id INT,
    question_text VARCHAR(200),
    answer_one varchar(30),
    answer_two VARCHAR(30),
    answer_three VARCHAR(30),
    answer_four VARCHAR(30),
    correct_answer INT
);

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    test_id INT,
    result FLOAT
);