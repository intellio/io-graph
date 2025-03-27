from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityInformationProtectionPolicySetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	defaultLabelId: Optional[str] = Field(alias="defaultLabelId", default=None,)
	isDowngradeJustificationRequired: Optional[bool] = Field(alias="isDowngradeJustificationRequired", default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory", default=None,)
	moreInfoUrl: Optional[str] = Field(alias="moreInfoUrl", default=None,)


