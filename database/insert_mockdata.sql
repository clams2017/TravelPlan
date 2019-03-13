INSERT INTO oreore_genre (genre_id, genre_name) VALUES (1, '動物園'), (2, '滝・渓谷'), (3, '河川');
INSERT INTO jaran_genre_small (jaran_genre_id, genre_small, genre_large) VALUES (1, '滝・渓谷', '自然景観・絶景');
INSERT INTO gurutabi_genre_small (gurutabi_genre_id, genre_small, genre_middle) VALUES (1, '動物園', '動物園・水族館'), (2, '滝・河川', '自然');
INSERT INTO jaran_genre (id, jaran_genre_id, oreore_genre_id) VALUES (1, 1, 2);
INSERT INTO gurutabi_genre (id, gurutabi_genre_id, oreore_genre_id) VALUES (1, 1, 1), (2, 2, 3), (3, 2, 2);
