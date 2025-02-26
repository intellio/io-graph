from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminRelationshipCustomerParticipant(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


