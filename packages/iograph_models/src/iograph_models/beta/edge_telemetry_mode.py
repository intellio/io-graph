from __future__ import annotations
from enum import StrEnum


class EdgeTelemetryMode(StrEnum):
	notConfigured = "notConfigured"
	intranet = "intranet"
	internet = "internet"
	intranetAndInternet = "intranetAndInternet"

