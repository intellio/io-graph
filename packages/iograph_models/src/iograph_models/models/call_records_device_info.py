from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsDeviceInfo(BaseModel):
	captureDeviceDriver: Optional[str] = Field(default=None,alias="captureDeviceDriver",)
	captureDeviceName: Optional[str] = Field(default=None,alias="captureDeviceName",)
	captureNotFunctioningEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	cpuInsufficentEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	deviceClippingEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	deviceGlitchEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	howlingEventCount: Optional[int] = Field(default=None,alias="howlingEventCount",)
	initialSignalLevelRootMeanSquare: Optional[float] | Optional[str] | ReferenceNumeric
	lowSpeechLevelEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	lowSpeechToNoiseEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	micGlitchRate: Optional[float] | Optional[str] | ReferenceNumeric
	receivedNoiseLevel: Optional[int] = Field(default=None,alias="receivedNoiseLevel",)
	receivedSignalLevel: Optional[int] = Field(default=None,alias="receivedSignalLevel",)
	renderDeviceDriver: Optional[str] = Field(default=None,alias="renderDeviceDriver",)
	renderDeviceName: Optional[str] = Field(default=None,alias="renderDeviceName",)
	renderMuteEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	renderNotFunctioningEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	renderZeroVolumeEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	sentNoiseLevel: Optional[int] = Field(default=None,alias="sentNoiseLevel",)
	sentSignalLevel: Optional[int] = Field(default=None,alias="sentSignalLevel",)
	speakerGlitchRate: Optional[float] | Optional[str] | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

