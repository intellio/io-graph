from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecureScore(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeUserCount: Optional[int] = Field(default=None,alias="activeUserCount",)
	averageComparativeScores: list[AverageComparativeScore] = Field(alias="averageComparativeScores",)
	azureTenantId: Optional[str] = Field(default=None,alias="azureTenantId",)
	controlScores: list[ControlScore] = Field(alias="controlScores",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	currentScore: Optional[float] | Optional[str] | ReferenceNumeric
	enabledServices: list[Optional[str]] = Field(alias="enabledServices",)
	licensedUserCount: Optional[int] = Field(default=None,alias="licensedUserCount",)
	maxScore: Optional[float] | Optional[str] | ReferenceNumeric
	vendorInformation: Optional[SecurityVendorInformation] = Field(default=None,alias="vendorInformation",)

from .average_comparative_score import AverageComparativeScore
from .control_score import ControlScore
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .security_vendor_information import SecurityVendorInformation

