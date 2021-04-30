CREATE DATABASE archive;

\c archive

CREATE TYPE archtypes AS ENUM ('Audio', 'Book', 'Game', 'ImageSet', 'Software', 'Video');
CREATE TYPE videotypes AS ENUM ('Anime', 'Anime Movie', 'CG Movie', 'Feature Film', 'Series', 'TV Series', 'Video', 'VR Live-Action', 'VR CG');
CREATE TYPE audiotypes AS ENUM ('ASMR', 'Audio Book', 'Audio Roleplay', 'Music');
CREATE TYPE booktypes AS ENUM ('Artbook', 'Comic', 'Doujinshi', 'Manga', 'Novel');
CREATE TYPE softtypes AS ENUM ('DCC', 'Driver', 'Reader');
CREATE TYPE imagetypes AS ENUM ('2D', 'CG', 'Photo');


CREATE TABLE games (
    uid INT GENERATED ALWAYS AS IDENTITY,
    archive INT NOT NULL,
    developer TEXT NOT NULL,
    title TEXT NOT NULL,
    genre TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    publisher TEXT,
    dlc TEXT[],
    id TEXT,
    drm TEXT,
    url TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE videos (
    uid INT GENERATED ALWAYS AS IDENTITY,
    archive INT NOT NULL,
    videotype videotypes NOT NULL,
    studio TEXT NOT NULL,
    title TEXT NOT NULL,
    genre TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    id TEXT,
    url TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE audio (
    uid INT GENERATED ALWAYS AS IDENTITY,
    archive INT NOT NULL,
    audiotype audiotypes NOT NULL,
    artist TEXT NOT NULL,
    title TEXT NOT NULL,
    adult BOOLEAN NOT NULL,
    publisher TEXT,
    id TEXT,
    drm TEXT,
    url TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE books (
    uid INT GENERATED ALWAYS AS IDENTITY,
    archive INT NOT NULL,
    booktype booktypes NOT NULL,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    genre TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    illus TEXT,
    id TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE software (
    uid INT GENERATED ALWAYS AS IDENTITY,
    archive INT NOT NULL,
    developer TEXT NOT NULL,
    title TEXT NOT NULL,
    softtype softtypes NOT NULL,
    version TEXT NOT NULL,
    format TEXT[],
    drm TEXT,
    url TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE imageset (
    uid INT GENERATED ALWAYS AS IDENTITY,
    archive INT NOT NULL,
    imagetype imagetypes NOT NULL,
    subject TEXT NOT NULL,
    title TEXT NOT NULL,
    filetype TEXT[] NOT NULL,
    adult BOOLEAN NOT NULL,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);
