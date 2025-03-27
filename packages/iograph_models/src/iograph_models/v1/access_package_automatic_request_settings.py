from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAutomaticRequestSettings(BaseModel):
	gracePeriodBeforeAccessRemoval: Optional[str] = Field(alias="gracePeriodBeforeAccessRemoval", default=None,)
	removeAccessWhenTargetLeavesAllowedTargets: Optional[bool] = Field(alias="removeAccessWhenTargetLeavesAllowedTargets", default=None,)
	requestAccessForAllowedTargets: Optional[bool] = Field(alias="requestAccessForAllowedTargets", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


