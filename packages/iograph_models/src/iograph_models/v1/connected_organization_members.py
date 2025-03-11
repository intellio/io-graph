from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConnectedOrganizationMembers(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	connectedOrganizationId: Optional[str] = Field(alias="connectedOrganizationId",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)


