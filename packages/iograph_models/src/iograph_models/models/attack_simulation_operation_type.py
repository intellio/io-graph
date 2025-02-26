from __future__ import annotations
from enum import Enum


class AttackSimulationOperationType(Enum):
	createSimualation = "createSimualation"
	updateSimulation = "updateSimulation"
	unknownFutureValue = "unknownFutureValue"

