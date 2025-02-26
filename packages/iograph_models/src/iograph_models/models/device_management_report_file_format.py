from __future__ import annotations
from enum import Enum


class DeviceManagementReportFileFormat(Enum):
	csv = "csv"
	pdf = "pdf"
	json = "json"
	unknownFutureValue = "unknownFutureValue"

