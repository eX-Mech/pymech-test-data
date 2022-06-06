// Gmsh project created on Sun Aug  2 19:03:55 2020
SetFactory("OpenCASCADE");

Point(1) = {0, 0, 0, 1.0};
Point(2) = {1, 0, 0, 1.0};
Point(3) = {1, 1, 0, 1.0};
Point(4) = {0, 1, 0, 1.0};

Line(1) = {4, 1};
Line(2) = {1, 2};
Line(3) = {2, 3};
Line(4) = {3, 4};

Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};
Transfinite Surface {1} = {4, 3, 2, 1};

Transfinite Line {1, 3} = 13 Using Progression 1; //12 elements in y
Transfinite Line {4, 2} = 17 Using Progression 1; //16 elements in x

Recombine Surface {1};

Extrude {0, 0, 1} {
  Surface{1}; Layers{8}; Recombine; //8 elements in z
}

Physical Surface("inlet") = {2};
Physical Surface("outlet") = {4};
Physical Surface("top") = {5};
Physical Surface("bottom") = {3};
Physical Surface("back") = {1};
Physical Surface("front") = {6};

Physical Volume("fluid") = {1};
