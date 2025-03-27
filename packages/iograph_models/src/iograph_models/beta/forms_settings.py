from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FormsSettings(BaseModel):
	isBingImageSearchEnabled: Optional[bool] = Field(alias="isBingImageSearchEnabled", default=None,)
	isExternalSendFormEnabled: Optional[bool] = Field(alias="isExternalSendFormEnabled", default=None,)
	isExternalShareCollaborationEnabled: Optional[bool] = Field(alias="isExternalShareCollaborationEnabled", default=None,)
	isExternalShareResultEnabled: Optional[bool] = Field(alias="isExternalShareResultEnabled", default=None,)
	isExternalShareTemplateEnabled: Optional[bool] = Field(alias="isExternalShareTemplateEnabled", default=None,)
	isInOrgFormsPhishingScanEnabled: Optional[bool] = Field(alias="isInOrgFormsPhishingScanEnabled", default=None,)
	isRecordIdentityByDefaultEnabled: Optional[bool] = Field(alias="isRecordIdentityByDefaultEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


