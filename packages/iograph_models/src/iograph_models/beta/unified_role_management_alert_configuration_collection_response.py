from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlertConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[UnifiedRoleManagementAlertConfiguration]]] = Field(alias="value",default=None,)

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

