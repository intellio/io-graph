from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsDeviceInfo(BaseModel):
	captureDeviceDriver: Optional[str] = Field(default=None,alias="captureDeviceDriver",)
	captureDeviceName: Optional[str] = Field(default=None,alias="captureDeviceName",)
	captureNotFunctioningEventRatio: float | str | ReferenceNumeric
	cpuInsufficentEventRatio: float | str | ReferenceNumeric
	deviceClippingEventRatio: float | str | ReferenceNumeric
	deviceGlitchEventRatio: float | str | ReferenceNumeric
	howlingEventCount: Optional[int] = Field(default=None,alias="howlingEventCount",)
	initialSignalLevelRootMeanSquare: float | str | ReferenceNumeric
	lowSpeechLevelEventRatio: float | str | ReferenceNumeric
	lowSpeechToNoiseEventRatio: float | str | ReferenceNumeric
	micGlitchRate: float | str | ReferenceNumeric
	receivedNoiseLevel: Optional[int] = Field(default=None,alias="receivedNoiseLevel",)
	receivedSignalLevel: Optional[int] = Field(default=None,alias="receivedSignalLevel",)
	renderDeviceDriver: Optional[str] = Field(default=None,alias="renderDeviceDriver",)
	renderDeviceName: Optional[str] = Field(default=None,alias="renderDeviceName",)
	renderMuteEventRatio: float | str | ReferenceNumeric
	renderNotFunctioningEventRatio: float | str | ReferenceNumeric
	renderZeroVolumeEventRatio: float | str | ReferenceNumeric
	sentNoiseLevel: Optional[int] = Field(default=None,alias="sentNoiseLevel",)
	sentSignalLevel: Optional[int] = Field(default=None,alias="sentSignalLevel",)
	speakerGlitchRate: float | str | ReferenceNumeric
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

