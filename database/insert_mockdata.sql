set foreign_key_checks=0;
TRUNCATE TABLE oreore_genre;
TRUNCATE TABLE jalan_genre_small;
TRUNCATE TABLE gurutabi_genre_small;
TRUNCATE TABLE jalan_genre;
TRUNCATE TABLE gurutabi_genre;
set foreign_key_checks = 1;

INSERT INTO oreore_genre (genre_id, genre_name) VALUES (1, '動物園'), (2, '滝・渓谷'), (3, '河川');
INSERT INTO jalan_genre_small (jalan_genre_id, genre_small, genre_large) VALUES (1, '動物', '動・植物'), (2, '滝・渓谷', '自然景観・絶景');
INSERT INTO gurutabi_genre_small (gurutabi_genre_id, genre_small, genre_middle) VALUES (1, '動物園', '動物園・水族館'), (2, '滝・河川', '自然');
INSERT INTO jalan_genre (id, jalan_genre_id, oreore_genre_id) VALUES (1, 1, 1), (2, 2, 2);
INSERT INTO gurutabi_genre (id, gurutabi_genre_id, oreore_genre_id) VALUES (1, 1, 1), (2, 2, 3), (3, 2, 2);
