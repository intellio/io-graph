from __future__ import annotations
from enum import Enum


class SensitivityLabelAssignmentMethod(Enum):
	standard = "standard"
	privileged = "privileged"
	auto = "auto"
	unknownFutureValue = "unknownFutureValue"

