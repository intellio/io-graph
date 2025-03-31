from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomerVoiceSettings(BaseModel):
	isInOrgFormsPhishingScanEnabled: Optional[bool] = Field(alias="isInOrgFormsPhishingScanEnabled", default=None,)
	isRecordIdentityByDefaultEnabled: Optional[bool] = Field(alias="isRecordIdentityByDefaultEnabled", default=None,)
	isRestrictedSurveyAccessEnabled: Optional[bool] = Field(alias="isRestrictedSurveyAccessEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

