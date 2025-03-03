from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecureScore(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeUserCount: Optional[int] = Field(default=None,alias="activeUserCount",)
	averageComparativeScores: Optional[list[AverageComparativeScore]] = Field(default=None,alias="averageComparativeScores",)
	azureTenantId: Optional[str] = Field(default=None,alias="azureTenantId",)
	controlScores: Optional[list[ControlScore]] = Field(default=None,alias="controlScores",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	currentScore: float | str | ReferenceNumeric
	enabledServices: Optional[list[str]] = Field(default=None,alias="enabledServices",)
	licensedUserCount: Optional[int] = Field(default=None,alias="licensedUserCount",)
	maxScore: float | str | ReferenceNumeric
	vendorInformation: Optional[SecurityVendorInformation] = Field(default=None,alias="vendorInformation",)

from .average_comparative_score import AverageComparativeScore
from .control_score import ControlScore
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .security_vendor_information import SecurityVendorInformation

