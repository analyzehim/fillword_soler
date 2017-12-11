#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import time

class WordMatr():
    def __init__(self, filename):
        with codecs.open(filename, 'r', encoding='utf8') as f:
            text = f.read()
        self.size = len(text.split('\r\n')[0])
        self.square = [[0 for x in range(self.size)] for x in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.square[i][j] = text.split('\r\n')[i][j].encode('utf8')
        return

    def __len__(self):
        return self.size

    def __str__(self):
        output = ''
        for i in range(self.size):
            for j in range(self.size):
                output += self.square[i][j]
                output += ' '
            output += '\n'
        return output


class WordSet():
    def __init__(self, filename):
        self.wordset = set()
        with open(filename, 'r') as f:
            for word in f:
                self.wordset.add(word.replace('\n', ''))


def search(s, A, B, i, j):
    s += (A[i][j])
    if (len(s)/2) == size:
        if s in set_words.wordset:
                print s, j+1, i+1
                return
        return

    B[i][j] = 1
    if i < len(A)-1:
        if B[i+1][j] == 0:
            search(s, A, B, i+1, j)
  
    if j < len(A)-1:
        if B[i][1+j] == 0:
            search(s, A, B, i, j+1)

    if i > 0:
        if B[i-1][j] == 0:
            search(s, A, B, i-1, j)
           
    if j > 0:
        if B[i][j-1] == 0:
            search(s, A, B, i, j-1)
    B[i][j] = 0
    return


def go():
    A = WordMatr('square.txt')
    global set_words
    global size
    set_words = WordSet('text.txt')
    B = [[0 for x in range(len(A))] for x in range(len(A))]
    s = ''
    for size in range(5, 12):
        for i in range(len(A)):
            for j in range(len(A)):
                search(s, A.square, B, i, j)

if __name__ == "__main__":
    timestamp = time.time()
    go()
    print time.time() - timestamp
