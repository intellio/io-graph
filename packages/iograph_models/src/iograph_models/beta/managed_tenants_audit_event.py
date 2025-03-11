from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsAuditEvent(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activity: Optional[str] = Field(alias="activity",default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime",default=None,)
	activityId: Optional[str] = Field(alias="activityId",default=None,)
	category: Optional[str] = Field(alias="category",default=None,)
	httpVerb: Optional[str] = Field(alias="httpVerb",default=None,)
	initiatedByAppId: Optional[str] = Field(alias="initiatedByAppId",default=None,)
	initiatedByUpn: Optional[str] = Field(alias="initiatedByUpn",default=None,)
	initiatedByUserId: Optional[str] = Field(alias="initiatedByUserId",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	requestBody: Optional[str] = Field(alias="requestBody",default=None,)
	requestUrl: Optional[str] = Field(alias="requestUrl",default=None,)
	tenantIds: Optional[str] = Field(alias="tenantIds",default=None,)
	tenantNames: Optional[str] = Field(alias="tenantNames",default=None,)


