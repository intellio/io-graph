from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DepTvOSEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	configurationEndpointUrl: Optional[str] = Field(alias="configurationEndpointUrl",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	enableAuthenticationViaCompanyPortal: Optional[bool] = Field(alias="enableAuthenticationViaCompanyPortal",default=None,)
	requireCompanyPortalOnSetupAssistantEnrolledDevices: Optional[bool] = Field(alias="requireCompanyPortalOnSetupAssistantEnrolledDevices",default=None,)
	requiresUserAuthentication: Optional[bool] = Field(alias="requiresUserAuthentication",default=None,)


