from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UpgradePostRequest(BaseModel):
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(alias="consentedPermissionSet", default=None,)

from .teams_app_permission_set import TeamsAppPermissionSet
