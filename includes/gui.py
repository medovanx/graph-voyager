from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtGui import *

from includes.helpers import resource_path
from includes.searching_algorithms import Algorithms
from includes.graph import Graph

Ui_MainWindow, QtBaseClass = uic.loadUiType(resource_path(r"assets\gui.ui"))
class GraphVoyager(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(resource_path(r"assets\icon.png")))
        self.setFixedSize(self.size())
        self.search_button.clicked.connect(self.search)
        self.init_graph()
        self.DLS_limit = self.findChild(QLineEdit, 'DLS_limit')
        self.DLS_limit.setVisible(False)
        self.algorithm_select.currentIndexChanged.connect(self._algorithm_is_DLS)

    def init_graph(self):
        self.GRAPH = Graph().GRAPH
        self.HEURISTICS = Graph().HEURISTICS
        self.source_location.addItems(self.GRAPH.keys())
        self.goal_location.addItems(self.GRAPH.keys())

    def search(self):
        selected_source_location = self.source_location.currentText()
        select_goal_location = self.goal_location.currentText()
        selected_algorithm = self.algorithm_select.currentText()
        self.cost.setText("")

        if selected_algorithm == "Breadth-First Search (BFS)":
            self.algorithm = Algorithms.BFS(self.GRAPH, selected_source_location, select_goal_location)
            self.result.setText(" ➜ ".join(map(str, self.algorithm)))
        elif selected_algorithm == "Uniform Cost Search (UCS)":
            self.algorithm = Algorithms.UCS(self.GRAPH, selected_source_location, select_goal_location)
            self.result.setText(" ➜ ".join(map(str, self.algorithm[1])))
            self.cost.setText("Cost: " + str(self.algorithm[0]))
        elif selected_algorithm == "Depth-First Search (DFS)":
            self.algorithm = Algorithms.DFS(self.GRAPH, selected_source_location, select_goal_location)
            self.result.setText(" ➜ ".join(map(str, self.algorithm)))
        elif selected_algorithm == "Depth-limited Search (DLS)":
            try:
                depth_limit = int(self.DLS_limit.text())
            except ValueError:
                self.result.setText("Depth limit must be an integer.")
                return
            self.algorithm = Algorithms.DLS(self.GRAPH, selected_source_location, select_goal_location, depth_limit)
            if self.algorithm is not None:
                self.result.setText(" ➜ ".join(map(str, self.algorithm)))
            else:
                self.result.setText(f"There's no path from {selected_source_location} to {select_goal_location} with depth limit {depth_limit}.")
        elif selected_algorithm == "Iterative Deepening Search (IDDFS)":
            self.algorithm = Algorithms.IDDFS(self.GRAPH, selected_source_location, select_goal_location)
            self.result.setText(" ➜ ".join(map(str, self.algorithm)))
        elif selected_algorithm == "Bidirectional Search (BDS)":
            self.algorithm = Algorithms.BDS(self.GRAPH, selected_source_location, select_goal_location)
            self.result.setText(" ➜ ".join(map(str, self.algorithm)))
        elif selected_algorithm == "Greedy Best-First Search (GBFS)":
            self.algorithm = Algorithms.GBFS(self.GRAPH, selected_source_location, select_goal_location, self.HEURISTICS)
            self.result.setText(" ➜ ".join(map(str, self.algorithm)))
        elif selected_algorithm == "A* Search":
            self.algorithm = Algorithms.AStar(self.GRAPH, selected_source_location, select_goal_location, self.HEURISTICS)
            self.result.setText(" ➜ ".join(map(str, self.algorithm[0])))
            self.cost.setText("Cost: " + str(self.algorithm[1]))

    def _algorithm_is_DLS(self):
        selected_algorithm = self.algorithm_select.currentText()
        if selected_algorithm == "Depth-limited Search (DLS)":
            self.DLS_limit.setVisible(True)
        else:
            self.DLS_limit.setVisible(False)