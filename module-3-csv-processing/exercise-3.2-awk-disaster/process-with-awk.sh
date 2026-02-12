#!/bin/bash
# Extract transaction amounts from bank export
# NOTE: This script has a bug. Can you find it?
awk -F',' '{print $3}' bank-export.csv | tail -n +2
