from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantAlertRuleDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ManagedTenantsManagedTenantAlertRuleDefinition]] = Field(alias="value",default=None,)

from .managed_tenants_managed_tenant_alert_rule_definition import ManagedTenantsManagedTenantAlertRuleDefinition

