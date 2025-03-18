import networkx as nx
import numpy as np

class CausalEnvironment:
    def __init__(self, dag, structural_equations, initial_state=None):
        """
        Initializes the causal environment.

        :param dag: A directed acyclic graph (DAG) representing the causal model.
        :param structural_equations: A dictionary mapping each node to a function that defines its update rule.
        :param initial_state: A dictionary defining initial values of variables.
        """
        self.dag = dag
        self.structural_equations = structural_equations
        self.state = initial_state if initial_state else {node: 0 for node in dag.nodes}

    def step(self, interventions=None):
        """
        Performs a step by updating the state of each variable in causal order.

        :param interventions: A dictionary specifying external interventions on variables.
        :return: Updated state of the system.
        """
        if interventions is None:
            interventions = {}

        order = list(nx.topological_sort(self.dag))
        new_state = self.state.copy()

        for node in order:
            if node in interventions:
                new_state[node] = interventions[node]
            else:
                parents = list(self.dag.predecessors(node))
                parent_values = {p: new_state[p] for p in parents}
                new_state[node] = self.structural_equations[node](**parent_values)

        self.state = new_state
        return new_state
