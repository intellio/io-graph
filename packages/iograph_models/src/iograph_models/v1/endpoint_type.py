from __future__ import annotations
from enum import StrEnum


class EndpointType(StrEnum):
	default = "default"
	voicemail = "voicemail"
	skypeForBusiness = "skypeForBusiness"
	skypeForBusinessVoipPhone = "skypeForBusinessVoipPhone"
	unknownFutureValue = "unknownFutureValue"

