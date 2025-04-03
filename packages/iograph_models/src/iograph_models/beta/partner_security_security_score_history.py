from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PartnerSecuritySecurityScoreHistory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partner.security.securityScoreHistory"] = Field(alias="@odata.type", default="#microsoft.graph.partner.security.securityScoreHistory")
	compliantRequirementsCount: Optional[int] = Field(alias="compliantRequirementsCount", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	score: float | str | ReferenceNumeric
	totalRequirementsCount: Optional[int] = Field(alias="totalRequirementsCount", default=None,)

from .reference_numeric import ReferenceNumeric
