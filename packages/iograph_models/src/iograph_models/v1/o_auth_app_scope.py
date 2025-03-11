from __future__ import annotations
from enum import StrEnum


class OAuthAppScope(StrEnum):
	unknown = "unknown"
	readCalendar = "readCalendar"
	readContact = "readContact"
	readMail = "readMail"
	readAllChat = "readAllChat"
	readAllFile = "readAllFile"
	readAndWriteMail = "readAndWriteMail"
	sendMail = "sendMail"
	unknownFutureValue = "unknownFutureValue"

