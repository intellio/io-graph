from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecureScore(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activeUserCount: Optional[int] = Field(alias="activeUserCount",default=None,)
	averageComparativeScores: Optional[list[AverageComparativeScore]] = Field(alias="averageComparativeScores",default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId",default=None,)
	controlScores: Optional[list[ControlScore]] = Field(alias="controlScores",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	currentScore: float | str | ReferenceNumeric
	enabledServices: Optional[list[str]] = Field(alias="enabledServices",default=None,)
	licensedUserCount: Optional[int] = Field(alias="licensedUserCount",default=None,)
	maxScore: float | str | ReferenceNumeric
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation",default=None,)

from .average_comparative_score import AverageComparativeScore
from .control_score import ControlScore
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .security_vendor_information import SecurityVendorInformation

