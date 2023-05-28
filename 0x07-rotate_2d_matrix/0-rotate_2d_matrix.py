#!/usr/bin/python3

"""Rotating a two-dimensional matrix 90degress clockwise"""

def rotate_2d_matrix(matrix):
 matrixLength = len(matrix)
 
 for i in range(matrixLength):
   for l in range(i, matrixLength):
     matrix[i][l], matrix[l][i] = matrix[l][i], matrix[i][l]
     
 for i in range(matrixLength):
   matrix[i] = matrix[i][::-1]
    
