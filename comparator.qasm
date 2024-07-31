OPENQASM 2.0;
include "qelib1.inc";

qreg b[4];
qreg aux[4];
creg c[1];
barrier b[0], b[1], b[2], b[3], aux[0], aux[1], aux[2], aux[3];

barrier b[0], b[1], b[2], b[3], aux[0], aux[1], aux[2], aux[3];
cx aux[0], b[0];
ccx b[0], aux[0], aux[1];
barrier b[0], b[1], b[2], b[3], aux[0], aux[1], aux[2], aux[3];
cx aux[1], b[1];
ccx b[1], aux[1], aux[0];
barrier b[0], b[1], b[2], b[3], aux[0], aux[1], aux[2], aux[3];
cx aux[0], b[2];
ccx b[2], aux[0], aux[2];
barrier b[0], b[1], b[2], b[3], aux[0], aux[1], aux[2], aux[3];
cx aux[2], b[3];
ccx b[3], aux[2], aux[3];
measure aux[3] -> c[0];
