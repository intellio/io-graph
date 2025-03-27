from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecurityAffectedResource(BaseModel):
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


