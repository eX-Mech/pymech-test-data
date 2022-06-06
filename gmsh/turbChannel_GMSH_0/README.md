# Introduction

This case is a copy of the example turbChannel, where the mesh is generated using GMSH instead of genbox.

# How to run the case

- create generate the mesh using GMSH : 
```
gmsh turbChannel.geo -3 -order 2 -format msh2 -o turbChannel.msh
```
- convert the mesh to Nek5000 with gmsh2nek :
```
gmsh2nek
Enter mesh dimension: 3
Input .msh file name: turbChannel
 total node number is        14025
 total quad element number is          832
 total hex element number is         1536
 ******************************************************
 Boundary info summary
 BoundaryName     BoundaryID
 inlet           1
 outlet           2
 top           3
 bottom           4
 back           5
 front           6
 ******************************************************
 Enter number of periodic boundary surface pairs:
2
 input surface 1 and  surface 2  BoundaryID
1,2
 input translation vector (surface 1 -> surface 2)
1,0,0
 input surface 1 and  surface 2  BoundaryID
5,6
 input translation vector (surface 1 -> surface 2)
0,0,1
 ******************************************************
 Please set boundary conditions to all non-periodic boundaries
 in .usr file usrdat2() subroutine
 ******************************************************

writing turbChannel.re2
```
- discretise, build and run the case :
```
genmap
makenek turbChannel
nekbmpi turbChannel 4
```
