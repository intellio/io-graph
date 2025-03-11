from __future__ import annotations
from enum import StrEnum


class UserDefaultAuthenticationMethodType(StrEnum):
	push = "push"
	oath = "oath"
	voiceMobile = "voiceMobile"
	voiceAlternateMobile = "voiceAlternateMobile"
	voiceOffice = "voiceOffice"
	sms = "sms"
	unknownFutureValue = "unknownFutureValue"

