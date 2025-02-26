from __future__ import annotations
from enum import Enum


class CallRecordsVideoCodec(Enum):
	unknown = "unknown"
	invalid = "invalid"
	av1 = "av1"
	h263 = "h263"
	h264 = "h264"
	h264s = "h264s"
	h264uc = "h264uc"
	h265 = "h265"
	rtvc1 = "rtvc1"
	rtVideo = "rtVideo"
	xrtvc1 = "xrtvc1"
	unknownFutureValue = "unknownFutureValue"

