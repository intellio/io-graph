from __future__ import annotations
from enum import StrEnum


class AuthenticationPhoneType(StrEnum):
	mobile = "mobile"
	alternateMobile = "alternateMobile"
	office = "office"
	unknownFutureValue = "unknownFutureValue"

