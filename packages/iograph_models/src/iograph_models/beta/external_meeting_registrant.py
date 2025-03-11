from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalMeetingRegistrant(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)


