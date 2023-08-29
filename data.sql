
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    birthdate DATE NOT NULL,
    country TEXT NOT NULL
    );

INSERT INTO users (username, email, birthdate, country) VALUES
    
('rrobbins', 'rhodesjoseph@example.org', '1977-01-13', 'Belarus'),
('williamcherry', 'paula91@example.org', '1998-12-10', 'Saint Martin'),
('david69', 'wallacetara@example.net', '2020-11-21', 'British Virgin Islands'),
('silvalawrence', 'justinerickson@example.net', '1970-09-05', 'Greenland'),
('anthony27', 'robertgray@example.org', '2008-06-25', 'Hong Kong')