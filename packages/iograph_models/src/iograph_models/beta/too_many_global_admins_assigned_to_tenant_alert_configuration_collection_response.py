from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TooManyGlobalAdminsAssignedToTenantAlertConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[TooManyGlobalAdminsAssignedToTenantAlertConfiguration]] = Field(alias="value",default=None,)

from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration

