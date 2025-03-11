from __future__ import annotations
from enum import StrEnum


class RecordCompletionReason(StrEnum):
	operationCanceled = "operationCanceled"
	stopToneDetected = "stopToneDetected"
	maxRecordDurationReached = "maxRecordDurationReached"
	initialSilenceTimeout = "initialSilenceTimeout"
	maxSilenceTimeout = "maxSilenceTimeout"
	playPromptFailed = "playPromptFailed"
	playBeepFailed = "playBeepFailed"
	mediaReceiveTimeout = "mediaReceiveTimeout"
	unspecifiedError = "unspecifiedError"

