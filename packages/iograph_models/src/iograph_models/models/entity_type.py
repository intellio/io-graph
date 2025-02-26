from __future__ import annotations
from enum import Enum


class EntityType(Enum):
	event = "event"
	message = "message"
	driveItem = "driveItem"
	externalItem = "externalItem"
	site = "site"
	list = "list"
	listItem = "listItem"
	drive = "drive"
	unknownFutureValue = "unknownFutureValue"
	chatMessage = "chatMessage"
	person = "person"
	acronym = "acronym"
	bookmark = "bookmark"

