from __future__ import annotations
from enum import StrEnum


class DeviceManagementReportFileFormat(StrEnum):
	csv = "csv"
	pdf = "pdf"
	json = "json"
	unknownFutureValue = "unknownFutureValue"

