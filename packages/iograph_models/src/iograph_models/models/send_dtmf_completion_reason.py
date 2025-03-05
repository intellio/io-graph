from __future__ import annotations
from enum import StrEnum


class SendDtmfCompletionReason(StrEnum):
	unknown = "unknown"
	completedSuccessfully = "completedSuccessfully"
	mediaOperationCanceled = "mediaOperationCanceled"
	unknownFutureValue = "unknownFutureValue"

