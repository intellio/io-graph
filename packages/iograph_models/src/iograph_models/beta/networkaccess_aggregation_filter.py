from __future__ import annotations
from enum import StrEnum


class NetworkaccessAggregationFilter(StrEnum):
	transactions = "transactions"
	users = "users"
	devices = "devices"
	unknownFutureValue = "unknownFutureValue"
	bytesSent = "bytesSent"
	bytesReceived = "bytesReceived"
	totalBytes = "totalBytes"

