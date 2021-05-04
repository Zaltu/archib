CREATE DATABASE archive;

\c archive

CREATE TYPE archtypes AS ENUM ('Audio', 'Book', 'Game', 'ImageSet', 'Software', 'Video');
CREATE TYPE videostyles AS ENUM ('Anime', 'Cartoon', 'CG', 'Live-Action');
CREATE TYPE videotypes AS ENUM ('Series', 'Feature');
CREATE TYPE audiotypes AS ENUM ('ASMR', 'Audio Book', 'Audio Roleplay', 'Music');
CREATE TYPE booktypes AS ENUM ('Artbook', 'Comic', 'Doujinshi', 'Manga', 'Novel');
CREATE TYPE softtypes AS ENUM ('DCC', 'Driver', 'Reader');
CREATE TYPE imagetypes AS ENUM ('2D', 'CG', 'Photo');


CREATE TABLE games (
    uid INT GENERATED ALWAYS AS IDENTITY,
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
    mod TEXT,
    gamever TEXT,
    notes TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE videos (
    uid INT GENERATED ALWAYS AS IDENTITY,
    videostyle videostyles NOT NULL,
    videotype videotypes NOT NULL,
    studio TEXT NOT NULL,
    title TEXT NOT NULL,
    genre TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    vr BOOLEAN NOT NULL,
    id TEXT,
    url TEXT,
    notes TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE audio (
    uid INT GENERATED ALWAYS AS IDENTITY,
    audiotype audiotypes NOT NULL,
    artist TEXT NOT NULL,
    title TEXT NOT NULL,
    adult BOOLEAN NOT NULL,
    publisher TEXT,
    id TEXT,
    drm TEXT,
    url TEXT,
    notes TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE books (
    uid INT GENERATED ALWAYS AS IDENTITY,
    booktype booktypes NOT NULL,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    genre TEXT[] NOT NULL,
    year INT NOT NULL,
    adult BOOLEAN NOT NULL,
    illus TEXT,
    id TEXT,
    notes TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE software (
    uid INT GENERATED ALWAYS AS IDENTITY,
    developer TEXT NOT NULL,
    title TEXT NOT NULL,
    softtype softtypes NOT NULL,
    version TEXT NOT NULL,
    format TEXT[],
    drm TEXT,
    url TEXT,
    notes TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);

CREATE TABLE imageset (
    uid INT GENERATED ALWAYS AS IDENTITY,
    imagetype imagetypes NOT NULL,
    subject TEXT NOT NULL,
    title TEXT NOT NULL,
    filetype TEXT[] NOT NULL,
    adult BOOLEAN NOT NULL,
    notes TEXT,
    filepath TEXT NOT NULL,
    archtype archtypes NOT NULL,
    displayname TEXT NOT NULL
);
