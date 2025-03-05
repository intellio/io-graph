from __future__ import annotations
from enum import StrEnum


class AttackSimulationOperationType(StrEnum):
	createSimualation = "createSimualation"
	updateSimulation = "updateSimulation"
	unknownFutureValue = "unknownFutureValue"

