#!/usr/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

from time import perf_counter

from zipfile import ZipFile

pass_count = 0

passList = input('Enter the password list : ')
zip_File_Name = input('Enter zip file : ')

passData = []

t_t = perf_counter()

with open(passList, 'r', encoding='utf-8', errors='ignore') as Data:
    for i in Data:
        passData.append(i[:-1])


def fetch(session, zipObj):

    # print(zipObj)

    zipObj.extractall(pwd=bytes(session, 'utf-8'))
    print ('Password : ', session, ' -- Time Taken : ', perf_counter()
           - t_t)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=500) as executor:
        with ZipFile(zip_File_Name, 'r') as zipObj:
            executor.map(fetch, passData, [zipObj] * len(passData))
            executor.shutdown(wait=True)
