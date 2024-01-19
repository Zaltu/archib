CREATE DATABASE archive;

\c archive

CREATE TYPE archtypes AS ENUM ('Audio', 'Book', 'Game', 'ImageSet', 'Software', 'Video');
CREATE TYPE videostyles AS ENUM ('Anime', 'Cartoon', 'CG', 'Live-Action');
CREATE TYPE videotypes AS ENUM ('Series', 'Feature');
CREATE TYPE audiotypes AS ENUM ('ASMR', 'Audiobook', 'Audio Roleplay', 'Music');
CREATE TYPE booktypes AS ENUM ('Artbook', 'Comic', 'Doujinshi', 'Manga', 'Novel', 'Magazine');
CREATE TYPE softtypes AS ENUM ('DCC', 'Driver', 'Reader');
CREATE TYPE imagetypes AS ENUM ('2D', 'CG', 'Photo');

CREATE TYPE gameextratypes AS ENUM ('DLC', 'Patch', 'Mod');


CREATE TABLE audios (
    uid INT GENERATED ALWAYS AS IDENTITY,
    audio_type audiotypes NOT NULL,
    artist TEXT NOT NULL,
    title TEXT NOT NULL,
    adult BOOLEAN NOT NULL,
    publisher TEXT,
    product_id TEXT,
    storefront TEXT,
    url TEXT,
    note TEXT,
    file_path TEXT NOT NULL,
    live_media BOOLEAN NOT NULL DEFAULT FALSE,
    display_name TEXT NOT NULL
);

CREATE TABLE books (
    uid INT GENERATED ALWAYS AS IDENTITY,
    book_type booktypes NOT NULL,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    genres TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    illus TEXT,
    product_id TEXT,
    note TEXT,
    file_path TEXT NOT NULL,
    live_media BOOLEAN NOT NULL DEFAULT FALSE,
    display_name TEXT NOT NULL
);

CREATE TABLE games (
    uid INT GENERATED ALWAYS AS IDENTITY,
    platform TEXT NOT NULL,
    developer TEXT NOT NULL,
    title TEXT NOT NULL,
    adult BOOLEAN NOT NULL,
    genres TEXT[],
    year INT,
    publisher TEXT,
    dlc TEXT[],
    product_id TEXT,
    storefront TEXT,
    drm TEXT[],
    url TEXT,
    gamever TEXT,
    note TEXT,
    file_path TEXT NOT NULL,
    display_name TEXT NOT NULL
);

CREATE TABLE imagesets (
    uid INT GENERATED ALWAYS AS IDENTITY,
    image_type imagetypes NOT NULL,
    artist TEXT,
    title TEXT NOT NULL,
    file_types TEXT[] NOT NULL,
    adult BOOLEAN NOT NULL,
    note TEXT,
    moving BOOLEAN NOT NULL DEFAULT FALSE,
    file_path TEXT NOT NULL,
    live_media BOOLEAN NOT NULL DEFAULT FALSE,
    display_name TEXT NOT NULL
);

CREATE TABLE software (
    uid INT GENERATED ALWAYS AS IDENTITY,
    soft_type softtypes NOT NULL,
    developer TEXT NOT NULL,
    title TEXT NOT NULL,
    version TEXT NOT NULL,
    formats TEXT[],
    storefront TEXT,
    url TEXT,
    note TEXT,
    file_path TEXT NOT NULL,
    display_name TEXT NOT NULL
);

CREATE TABLE videos (
    uid INT GENERATED ALWAYS AS IDENTITY,
    video_type videotypes NOT NULL,
    video_style videostyles NOT NULL,
    studio TEXT NOT NULL,
    title TEXT NOT NULL,
    genres TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    vr BOOLEAN NOT NULL,
    product_id TEXT,
    url TEXT,
    note TEXT,
    file_path TEXT NOT NULL,
    live_media BOOLEAN NOT NULL DEFAULT FALSE,
    display_name TEXT NOT NULL
);


CREATE TABLE genres (
    uid INT GENERATED ALWAYS AS IDENTITY,
    title TEXT NOT NULL,
    note TEXT
);
CREATE TABLE gameextras (
    uid INT GENERATED ALWAYS AS IDENTITY,
    title TEXT NOT NULL,
    game_extra_type gameextratypes NOT NULL,
    included BOOLEAN NOT NULL,
    note TEXT,
    file_path TEXT
);
CREATE TABLE filetypes (
    uid INT GENERATED ALWAYS AS IDENTITY,
    title TEXT NOT NULL,
    extension TEXT,
    note TEXT
);