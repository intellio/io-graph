from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAutomaticRequestSettings(BaseModel):
	gracePeriodBeforeAccessRemoval: Optional[str] = Field(default=None,alias="gracePeriodBeforeAccessRemoval",)
	removeAccessWhenTargetLeavesAllowedTargets: Optional[bool] = Field(default=None,alias="removeAccessWhenTargetLeavesAllowedTargets",)
	requestAccessForAllowedTargets: Optional[bool] = Field(default=None,alias="requestAccessForAllowedTargets",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


