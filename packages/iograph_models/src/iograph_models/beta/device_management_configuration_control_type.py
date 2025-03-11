from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationControlType(StrEnum):
	default = "default"
	dropdown = "dropdown"
	smallTextBox = "smallTextBox"
	largeTextBox = "largeTextBox"
	toggle = "toggle"
	multiheaderGrid = "multiheaderGrid"
	contextPane = "contextPane"
	unknownFutureValue = "unknownFutureValue"

