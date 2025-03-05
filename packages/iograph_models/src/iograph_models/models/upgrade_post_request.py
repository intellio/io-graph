from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpgradePostRequest(BaseModel):
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(default=None,alias="consentedPermissionSet",)

from .teams_app_permission_set import TeamsAppPermissionSet

