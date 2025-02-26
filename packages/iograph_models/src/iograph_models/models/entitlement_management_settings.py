from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EntitlementManagementSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	durationUntilExternalUserDeletedAfterBlocked: Optional[str] = Field(default=None,alias="durationUntilExternalUserDeletedAfterBlocked",)
	externalUserLifecycleAction: Optional[AccessPackageExternalUserLifecycleAction] = Field(default=None,alias="externalUserLifecycleAction",)

from .access_package_external_user_lifecycle_action import AccessPackageExternalUserLifecycleAction

