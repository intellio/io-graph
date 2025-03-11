from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsRemoteConnection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudPcFailurePercentage: float | str | ReferenceNumeric
	cloudPcRoundTripTime: float | str | ReferenceNumeric
	cloudPcSignInTime: float | str | ReferenceNumeric
	coreBootTime: float | str | ReferenceNumeric
	coreSignInTime: float | str | ReferenceNumeric
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	remoteSignInTime: float | str | ReferenceNumeric
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	virtualNetwork: Optional[str] = Field(alias="virtualNetwork",default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

