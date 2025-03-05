from __future__ import annotations
from enum import StrEnum


class SensitivityLabelAssignmentMethod(StrEnum):
	standard = "standard"
	privileged = "privileged"
	auto = "auto"
	unknownFutureValue = "unknownFutureValue"

