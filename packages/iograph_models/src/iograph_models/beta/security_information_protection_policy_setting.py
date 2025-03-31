from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityInformationProtectionPolicySetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.informationProtectionPolicySetting"] = Field(alias="@odata.type",)
	defaultLabelId: Optional[str] = Field(alias="defaultLabelId", default=None,)
	isDowngradeJustificationRequired: Optional[bool] = Field(alias="isDowngradeJustificationRequired", default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory", default=None,)
	moreInfoUrl: Optional[str] = Field(alias="moreInfoUrl", default=None,)

