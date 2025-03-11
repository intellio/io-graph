from __future__ import annotations
from enum import StrEnum


class ResponseType(StrEnum):
	none = "none"
	organizer = "organizer"
	tentativelyAccepted = "tentativelyAccepted"
	accepted = "accepted"
	declined = "declined"
	notResponded = "notResponded"

