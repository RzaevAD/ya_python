from typing import List
import numpy as np
import json


def unique_tags(payload: dict)->List[str]:
    # исправьте ошибку
    payload = payload.get('tags', [])

    res = set(list(map(lambda x: (x, type(x)), payload)))
    res = [i[0] for i in res]
    
    return res


if __name__ == '__main__':
    data = '''
    {
        "title": "Звездные войны 1: Империя приносит баги",
        "description": "Эпичная сага по поиску багов в старом легаси проекте Империи",
    "tags": [2, "семейное кино", "космос", 1.0, 2.0, "2", "сага", "эпик", "добро против зла", true, "челмедведосвин", "debug", "ipdb", "PyCharm", "боевик", "боевик", "эникей", "дарт багус", 5, 6,4, "блокбастер", "кино 2020", 7, 3, 9, 12, "каникулы в космосе", "коварство"],
    "version": 17
    }
    '''

    print(unique_tags(json.loads(data)))
