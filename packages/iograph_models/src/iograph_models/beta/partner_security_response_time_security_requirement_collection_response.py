from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecurityResponseTimeSecurityRequirementCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PartnerSecurityResponseTimeSecurityRequirement]] = Field(alias="value",default=None,)

from .partner_security_response_time_security_requirement import PartnerSecurityResponseTimeSecurityRequirement

