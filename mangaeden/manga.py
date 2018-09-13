# -*- coding: utf-8 -*-

""" Mangaeden Manga Module """

import typing

Manga = typing.NewType('Manga', dict)
STATUS = ['', 'Ongoing', 'Completed']


def get_alias(manga: Manga) -> str:
    """Gets the alias."""
    return manga['alias']

def get_artist(manga: Manga) -> str:
    """Gets the artist."""
    return manga['artist']

def get_author(manga: Manga) -> str:
    """Gets the author."""
    return manga['author']

def get_categories(manga: Manga) -> list:
    """Gets categories list."""
    return manga['categories']

def get_chapters(manga: Manga) -> list([]):
    """Gets chapters list."""
    return manga['chapters']

def get_creation_date(manga: Manga) -> float:
    """Gets creation date."""
    return manga['created']

def get_number_of_chapters(manga: Manga) -> int:
    """Gets the number of chapters."""
    return manga['chapters_len']

def get_description(manga: Manga) -> str:
    """Gets description."""
    return manga['description'].strip('\n')

def get_number_of_views(manga: Manga) -> int:
    """Gets the number of views."""
    return manga['hits']

def get_cover(manga: Manga) -> str:
    """Gets cover image url."""
    return manga['image']

def get_language(manga: Manga) -> int:
    """Gets language code."""
    return manga['language']

def get_last_chapter_date(manga: Manga) -> float:
    """Gets last chapter unix timestamp code."""
    return manga['last_chapter_date']

def get_release_year(manga: Manga) -> int:
    """Gets release year."""
    return manga['released']

def get_status(manga: Manga) -> int:
    """Gets status code."""
    return manga['status']

def get_title(manga: Manga) -> str:
    """Gets title."""
    return manga['title']
