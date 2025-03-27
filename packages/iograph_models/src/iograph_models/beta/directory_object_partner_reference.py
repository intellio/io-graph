from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DirectoryObjectPartnerReference(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.directoryObjectPartnerReference"] = Field(alias="@odata.type", default="#microsoft.graph.directoryObjectPartnerReference")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalPartnerTenantId: Optional[UUID] = Field(alias="externalPartnerTenantId", default=None,)
	objectType: Optional[str] = Field(alias="objectType", default=None,)


