from __future__ import annotations
from enum import StrEnum


class CallRecordsAudioCodec(StrEnum):
	unknown = "unknown"
	invalid = "invalid"
	cn = "cn"
	pcma = "pcma"
	pcmu = "pcmu"
	amrWide = "amrWide"
	g722 = "g722"
	g7221 = "g7221"
	g7221c = "g7221c"
	g729 = "g729"
	multiChannelAudio = "multiChannelAudio"
	muchv2 = "muchv2"
	opus = "opus"
	satin = "satin"
	satinFullband = "satinFullband"
	rtAudio8 = "rtAudio8"
	rtAudio16 = "rtAudio16"
	silk = "silk"
	silkNarrow = "silkNarrow"
	silkWide = "silkWide"
	siren = "siren"
	xmsRta = "xmsRta"
	unknownFutureValue = "unknownFutureValue"

