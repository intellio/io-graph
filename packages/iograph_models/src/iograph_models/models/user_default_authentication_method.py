from __future__ import annotations
from enum import Enum


class UserDefaultAuthenticationMethod(Enum):
	push = "push"
	oath = "oath"
	voiceMobile = "voiceMobile"
	voiceAlternateMobile = "voiceAlternateMobile"
	voiceOffice = "voiceOffice"
	sms = "sms"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

