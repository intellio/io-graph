from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EntitlementManagementSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	durationUntilExternalUserDeletedAfterBlocked: Optional[str] = Field(alias="durationUntilExternalUserDeletedAfterBlocked",default=None,)
	externalUserLifecycleAction: Optional[AccessPackageExternalUserLifecycleAction | str] = Field(alias="externalUserLifecycleAction",default=None,)

from .access_package_external_user_lifecycle_action import AccessPackageExternalUserLifecycleAction

