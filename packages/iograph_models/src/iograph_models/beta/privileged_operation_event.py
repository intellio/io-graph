from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedOperationEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	referenceKey: Optional[str] = Field(alias="referenceKey", default=None,)
	referenceSystem: Optional[str] = Field(alias="referenceSystem", default=None,)
	requestorId: Optional[str] = Field(alias="requestorId", default=None,)
	requestorName: Optional[str] = Field(alias="requestorName", default=None,)
	requestType: Optional[str] = Field(alias="requestType", default=None,)
	roleId: Optional[str] = Field(alias="roleId", default=None,)
	roleName: Optional[str] = Field(alias="roleName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userMail: Optional[str] = Field(alias="userMail", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)


