#!bin/bash
mkdir original_data
cp -n *W[12]data.txt original_data
matlab18 < transform_data.m > /dev/null
