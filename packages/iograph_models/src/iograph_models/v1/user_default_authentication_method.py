from __future__ import annotations
from enum import StrEnum


class UserDefaultAuthenticationMethod(StrEnum):
	push = "push"
	oath = "oath"
	voiceMobile = "voiceMobile"
	voiceAlternateMobile = "voiceAlternateMobile"
	voiceOffice = "voiceOffice"
	sms = "sms"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

