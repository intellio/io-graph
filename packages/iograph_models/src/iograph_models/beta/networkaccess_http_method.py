from __future__ import annotations
from enum import StrEnum


class NetworkaccessHttpMethod(StrEnum):
	get = "get"
	post = "post"
	put = "put"
	delete = "delete"
	head = "head"
	options = "options"
	connect = "connect"
	patch = "patch"
	trace = "trace"
	unknownFutureValue = "unknownFutureValue"

