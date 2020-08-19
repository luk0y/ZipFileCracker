#!/usr/bin/python
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

from time import perf_counter

from zipfile import ZipFile

pass_count = 0

passList = input('Enter the password list : ')

passData = []

t_t = perf_counter()

with open(passList, 'r', encoding='utf-8', errors='ignore') as Data:
    for i in Data:
        passData.append(i[:-1])


def fetch(session, zipObj):

    # print(session)

    global count

    count = count + 1

    zipObj.extractall(pwd=bytes(session, 'utf-8'))
    print (
        'Password : ',
        session,
        ' -- Time Taken : ',
        perf_counter() - t_t,
        ' -- Password Count : ',
        pass_count,
        )


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=500) as executor:
        zipObj = ZipFile('testingFile.zip', 'r')
        with ZipFile('testingFile.zip', 'r') as zipObj:
            executor.map(fetch, passData, [zipObj] * len(passData))
            executor.shutdown(wait=True)
