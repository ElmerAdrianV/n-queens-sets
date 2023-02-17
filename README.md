# n-queens-sets
This repo solve the n-Queens problem using sets, returning all the possible solutions

The methodolgy using is recurvisely:
  - create a nxn board
  - place randomly a queen at pop one unknown square.
  - calculate using sets all the squares unavailable of placing that queen
  - if we place n queens and if unique the solution, saves in a lists
  - return a list with all the solutions
