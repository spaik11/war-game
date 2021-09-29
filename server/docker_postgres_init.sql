CREATE TABLE IF NOT EXISTS users
(
    id int PRIMARY KEY,
    username CHAR(50) NOT NULL,
    password CHAR(50) NOT NULL,
    record int NOT NULL
);

INSERT INTO users (id, username, password, record) VALUES
(
    1,
    'sung',
    '123',
    0
),
(
    2,
    'bob',
    '123',
    0
),
(
    3,
    'nancy',
    '123',
    0
),
(
    4,
    'robert',
    '123',
    0
);