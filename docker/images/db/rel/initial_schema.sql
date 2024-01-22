CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS POSTGIS;
CREATE EXTENSION IF NOT EXISTS POSTGIS_TOPOLOGY;

CREATE TABLE public.countries (
	id              uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	name            VARCHAR(250) UNIQUE NOT NULL,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE public.artists (
	id              uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	name            VARCHAR(250) UNIQUE NOT NULL,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE public.albums (
	id              uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	name            VARCHAR(250) UNIQUE NOT NULL,
    release_date    DATE UNIQUE NOT NULL,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE public.musics (
	id              uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    spotify_id      VARCHAR(250) NOT NULL,
	name            VARCHAR(250) NOT NULL,
	album_id        uuid,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE public.artists_musics (
    artist_id       uuid UNIQUE NOT NULL REFERENCES artists (id),
    music_id        uuid UNIQUE NOT NULL REFERENCES musics (id)
);
ALTER TABLE artists_musics
    ADD CONSTRAINT artists_musics_pkey
        PRIMARY KEY (artist_id,music_id);
ALTER TABLE musics
    ADD CONSTRAINT musics_albums_id_fk
        FOREIGN KEY (album_id) REFERENCES albums
            ON DELETE CASCADE;

/* Sample table and data that we can insert once the database is created for the first time */

INSERT INTO public.countries (id, name, created_on, updated_on) VALUES ('34e2344c-1b45-4ead-a5b2-3e20300d5875', 'PT', '2024-01-22 00:52:30.670275', '2024-01-22 00:52:30.670275');
INSERT INTO public.artists (id, name, created_on, updated_on) VALUES ('38be47fa-30ea-46f2-b06a-e15f59c170f4', 'testartist', '2024-01-22 00:52:49.104179', '2024-01-22 00:52:49.104179');
INSERT INTO public.albums (id, name, release_date, created_on, updated_on) VALUES ('c3b797ee-6d1e-4e5f-ad32-2b5a63388115', 'teste', '2024-01-11', '2024-01-22 00:50:48.399138', '2024-01-22 00:50:48.399138');
INSERT INTO public.musics (id, spotify_id, name, album_id, created_on, updated_on) VALUES ('28f55446-a1c7-488e-b6c0-d1d27c315365', '443243242321', 'songtest', 'c3b797ee-6d1e-4e5f-ad32-2b5a63388115', '2024-01-22 00:51:31.153039', '2024-01-22 00:51:31.153039');
INSERT INTO public.musics (id, spotify_id, name, album_id, created_on, updated_on) VALUES ('d5792a2e-4db3-40f6-bbd7-483c62feb15f', '321321212211', 'songtest2', 'c3b797ee-6d1e-4e5f-ad32-2b5a63388115', '2024-01-22 00:51:50.628976', '2024-01-22 00:51:50.628976');


