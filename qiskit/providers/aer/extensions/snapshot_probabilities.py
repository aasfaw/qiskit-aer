# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals

"""
Simulator command to snapshot internal simulator representation.
"""

from qiskit import QuantumCircuit
from qiskit.providers.aer.extensions import Snapshot


class SnapshotProbabilites(Snapshot):
    """Snapshot instruction for all methods of Qasm simulator."""

    def __init__(self,
                 label,
                 num_qubits=0,
                 num_clbits=0,
                 variance=False,
                 params=None,):

        if variance:
            super().__init__(label, 'probabilities_with_variance', num_qubits, num_clbits, params)
        else:
            super().__init__(label, 'probabilities', num_qubits, num_clbits, params)


def snapshot_probabilities(self,
                           label,
                           qubits=None,
                           variance=False,
                           params=None):
    """Take a snapshot of the internal simulator representation.
    Works on specified qubits or the full register, and prevents reordering (like barrier).
    Args:
        label (str): a snapshot label to report the result
        qubits (list or None): the qubits to apply snapshot to [Default: None]
        variance (bool): set snapshot_type to 'probabilities' or '
                         probabilities_with_variance' [Default: False]
        params (list or None): the parameters for snapshot_type [Default: None]
    Returns:
        QuantumCircuit: with attached command
    Raises:
        ExtensionError: malformed command
    """
    snapshot_register = Snapshot.define_snapshot_register(self, label, qubits)

    return self.append(
        SnapshotProbabilites(label,
                             num_qubits=len(snapshot_register),
                             variance=variance,
                             params=params), snapshot_register)


QuantumCircuit.snapshot_probabilities = snapshot_probabilities
