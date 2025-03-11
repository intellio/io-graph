from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceConfigurationUserStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	compliantUserCount: Optional[int] = Field(alias="compliantUserCount",default=None,)
	conflictUserCount: Optional[int] = Field(alias="conflictUserCount",default=None,)
	errorUserCount: Optional[int] = Field(alias="errorUserCount",default=None,)
	nonCompliantUserCount: Optional[int] = Field(alias="nonCompliantUserCount",default=None,)
	notApplicableUserCount: Optional[int] = Field(alias="notApplicableUserCount",default=None,)
	remediatedUserCount: Optional[int] = Field(alias="remediatedUserCount",default=None,)
	unknownUserCount: Optional[int] = Field(alias="unknownUserCount",default=None,)


