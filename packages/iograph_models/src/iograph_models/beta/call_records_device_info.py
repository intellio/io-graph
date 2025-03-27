from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsDeviceInfo(BaseModel):
	captureDeviceDriver: Optional[str] = Field(alias="captureDeviceDriver", default=None,)
	captureDeviceName: Optional[str] = Field(alias="captureDeviceName", default=None,)
	captureNotFunctioningEventRatio: float | str | ReferenceNumeric
	cpuInsufficentEventRatio: float | str | ReferenceNumeric
	deviceClippingEventRatio: float | str | ReferenceNumeric
	deviceGlitchEventRatio: float | str | ReferenceNumeric
	howlingEventCount: Optional[int] = Field(alias="howlingEventCount", default=None,)
	initialSignalLevelRootMeanSquare: float | str | ReferenceNumeric
	lowSpeechLevelEventRatio: float | str | ReferenceNumeric
	lowSpeechToNoiseEventRatio: float | str | ReferenceNumeric
	micGlitchRate: float | str | ReferenceNumeric
	receivedNoiseLevel: Optional[int] = Field(alias="receivedNoiseLevel", default=None,)
	receivedSignalLevel: Optional[int] = Field(alias="receivedSignalLevel", default=None,)
	renderDeviceDriver: Optional[str] = Field(alias="renderDeviceDriver", default=None,)
	renderDeviceName: Optional[str] = Field(alias="renderDeviceName", default=None,)
	renderMuteEventRatio: float | str | ReferenceNumeric
	renderNotFunctioningEventRatio: float | str | ReferenceNumeric
	renderZeroVolumeEventRatio: float | str | ReferenceNumeric
	sentNoiseLevel: Optional[int] = Field(alias="sentNoiseLevel", default=None,)
	sentSignalLevel: Optional[int] = Field(alias="sentSignalLevel", default=None,)
	speakerGlitchRate: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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

