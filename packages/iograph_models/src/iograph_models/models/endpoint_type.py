from __future__ import annotations
from enum import Enum


class EndpointType(Enum):
	default = "default"
	voicemail = "voicemail"
	skypeForBusiness = "skypeForBusiness"
	skypeForBusinessVoipPhone = "skypeForBusinessVoipPhone"
	unknownFutureValue = "unknownFutureValue"

