from __future__ import annotations
from enum import StrEnum


class EntityType(StrEnum):
	event = "event"
	message = "message"
	driveItem = "driveItem"
	externalItem = "externalItem"
	site = "site"
	list = "list"
	listItem = "listItem"
	drive = "drive"
	unknownFutureValue = "unknownFutureValue"
	acronym = "acronym"
	bookmark = "bookmark"
	chatMessage = "chatMessage"
	person = "person"
	qna = "qna"

