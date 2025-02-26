from __future__ import annotations
from enum import Enum


class SendDtmfCompletionReason(Enum):
	unknown = "unknown"
	completedSuccessfully = "completedSuccessfully"
	mediaOperationCanceled = "mediaOperationCanceled"
	unknownFutureValue = "unknownFutureValue"

