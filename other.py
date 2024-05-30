from __future__ import annotations
import numpy as np
import csv

def getDivisor(n):
    divisors=[(1,n)]
    i=2
    maxDivisor=n
    while i<maxDivisor:
        if n%i==0:
            divisors.append((i, n//i))
            maxDivisor=n//i
        i+=1
    return divisors
    
def displayGrid(grid):
    print('\n')
    for ligne in grid:
        for element in ligne:
            print(element, end='   ')
        print('\n')
        

def createGrid(numberRow: int, numberColumn: int):
    grid = [[0 for _ in range(numberColumn)] for _ in range(numberRow)]
    return grid

def gridToCSV(grid):
    newGrid=createGrid(len(grid), len(grid[0]))
    for i in range(len(newGrid)):
        for j in range(len(newGrid[i])):
            newGrid[i][j]=grid[i][j][0]
            
    with open('plan.csv', 'w') as file:
        for row in newGrid:
            for element in row:
                file.write(element)
                if row[-1]!=element:
                    file.write(',')
            file.write('\n')