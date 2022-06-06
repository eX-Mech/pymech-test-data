// Gmsh project created on Thu Apr 15 09:55:43 2021
SetFactory("OpenCASCADE");

height = 0.5;
n_h = 5;
gamma_h = 1.3;

width = 3.14;
n_w = 13;
gamma_w = 1;

length = 6.28;
n_l = 16;

Point(1) = {0, 0, 0, 1.0};
Point(2) = {width, 0, 0, 1.0};
Point(3) = {width, height, 0, 1.0};
Point(4) = {0, height, 0, 1.0};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Line Loop(1) = {4, 1, 2, 3};
Plane Surface(1) = {1};
Transfinite Surface {1} = {1, 2, 3, 4};

Transfinite Line {-4, 2} = n_h Using Progression gamma_h;
Transfinite Line {3, -1} = n_w Using Progression gamma_w;

Recombine Surface {1};
Extrude {0, 0, length} {
  Surface{1}; Layers{n_l}; Recombine;
}

Physical Surface("inlet") = {6};
Physical Surface("left") = {2};
Physical Surface("right") = {4};
Physical Surface("bottom") = {3};
Physical Surface("top") = {5};
Physical Surface("outlet") = {1};

Physical Volume("fluid") = {1};
