from __future__ import annotations
from enum import Enum


class OAuthAppScope(Enum):
	unknown = "unknown"
	readCalendar = "readCalendar"
	readContact = "readContact"
	readMail = "readMail"
	readAllChat = "readAllChat"
	readAllFile = "readAllFile"
	readAndWriteMail = "readAndWriteMail"
	sendMail = "sendMail"
	unknownFutureValue = "unknownFutureValue"

