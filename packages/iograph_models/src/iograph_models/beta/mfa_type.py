from __future__ import annotations
from enum import StrEnum


class MfaType(StrEnum):
	eotp = "eotp"
	oneWaySms = "oneWaySms"
	twoWaySms = "twoWaySms"
	twoWaySmsOtherMobile = "twoWaySmsOtherMobile"
	phoneAppNotification = "phoneAppNotification"
	phoneAppOtp = "phoneAppOtp"
	twoWayVoiceMobile = "twoWayVoiceMobile"
	twoWayVoiceOffice = "twoWayVoiceOffice"
	twoWayVoiceOtherMobile = "twoWayVoiceOtherMobile"
	fido = "fido"
	certificate = "certificate"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

