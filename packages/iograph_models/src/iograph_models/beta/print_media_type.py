from __future__ import annotations
from enum import StrEnum


class PrintMediaType(StrEnum):
	stationery = "stationery"
	transparency = "transparency"
	envelope = "envelope"
	envelopePlain = "envelopePlain"
	continuous = "continuous"
	screen = "screen"
	screenPaged = "screenPaged"
	continuousLong = "continuousLong"
	continuousShort = "continuousShort"
	envelopeWindow = "envelopeWindow"
	multiPartForm = "multiPartForm"
	multiLayer = "multiLayer"
	labels = "labels"

