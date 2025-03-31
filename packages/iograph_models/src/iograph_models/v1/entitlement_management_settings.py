from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EntitlementManagementSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.entitlementManagementSettings"] = Field(alias="@odata.type",)
	durationUntilExternalUserDeletedAfterBlocked: Optional[str] = Field(alias="durationUntilExternalUserDeletedAfterBlocked", default=None,)
	externalUserLifecycleAction: Optional[AccessPackageExternalUserLifecycleAction | str] = Field(alias="externalUserLifecycleAction", default=None,)

from .access_package_external_user_lifecycle_action import AccessPackageExternalUserLifecycleAction
