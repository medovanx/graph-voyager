<div align="center">

#  Graph Voyager
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![PyPI version](https://img.shields.io/pypi/pyversions/spotDL?color=%2344CC11&style=flat-square)](https://www.python.org/)
<div align="center">
<img src="https://i.imgur.com/SWbbzDS.png" width="40%">
</div>
<p style="font-size:20px;">
Graph Voyager is a Python program that explores various search algorithms on the Romania Map. The program provides an interactive interface for selecting different search algorithms to find paths from a source location to a goal location. <br><br>
Note: It's only to demonstrate how search algorithms work.</p>
</div>

# GUI
<p align="center">
  <img src="https://i.imgur.com/HPKy1V3.png" width="49%">
  <img src="https://i.imgur.com/gEVOdYD.png" width="49%">
</p>

# Supported Algorithms

<ol style="font-size:20px;">
  <li>Breadth-First Search (BFS)</li>
  <li>Uniform Cost Search (UCS)</li>
  <li>Depth-First Search (DFS)</li>
  <li>Depth-Limited Search (DLS)</li>
  <li>Iterative Deepening Search (IDDFS)</li>
  <li>Bidirectional Search (BDS)</li>
  <li>Greedy Best-First Search (GBFS)</li>
  <li>A* Search</li>
</ol>

# Hotrun (without compiling)
### 1. **Create and Activate Virtual Environment**

- **Create the Virtual Environment**:  
   Open your terminal and run the following command to create a virtual environment:
   ```bash
   python -m venv .venv
### 2. **Activate the Virtual Environment**:
  - On Windows:
    ```bash
    .venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```
### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
### 4. **Run the Python Application**
```bash
python main.py
```
> **Note 1**: Make sure to activate the virtual environment every time you start working on the project to ensure that the correct dependencies are used.

> **Note 2**: There's a precompiled binary in the Releases section you can download [here](https://github.com/medovanx/graph-voyager/releases/tag/v1)


# How to Use
- Run the program, you can downloada prebuilt release from the releases page.
- Select the desired search algorithm from the available options.
- Specify the source and goal locations.
- Press Search.

# Authors
- Mohamed Darwesh [@medovanx](https://github.com/medovanx)


<p style="font-size:16px;">Feel free to contribute and enhance Graph Voyager by adding more algorithms or improving the existing ones. Happy graph traversing!</p>
