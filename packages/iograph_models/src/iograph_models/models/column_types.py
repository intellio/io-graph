from __future__ import annotations
from enum import Enum


class ColumnTypes(Enum):
	note = "note"
	text = "text"
	choice = "choice"
	multichoice = "multichoice"
	number = "number"
	currency = "currency"
	dateTime = "dateTime"
	lookup = "lookup"
	boolean = "boolean"
	user = "user"
	url = "url"
	calculated = "calculated"
	location = "location"
	geolocation = "geolocation"
	term = "term"
	multiterm = "multiterm"
	thumbnail = "thumbnail"
	approvalStatus = "approvalStatus"
	unknownFutureValue = "unknownFutureValue"

