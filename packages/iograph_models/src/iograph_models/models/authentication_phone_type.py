from __future__ import annotations
from enum import Enum


class AuthenticationPhoneType(Enum):
	mobile = "mobile"
	alternateMobile = "alternateMobile"
	office = "office"
	unknownFutureValue = "unknownFutureValue"

