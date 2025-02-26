from __future__ import annotations
from enum import Enum


class ResponseType(Enum):
	none = "none"
	organizer = "organizer"
	tentativelyAccepted = "tentativelyAccepted"
	accepted = "accepted"
	declined = "declined"
	notResponded = "notResponded"

