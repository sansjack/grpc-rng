# tests/conftest.py
import sys
import os

# Assuming your directory structure is:
# Developer/
# ├── grpc-rng/
# │   ├── src/
# │   └── tests/
# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
