from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenantAlertRuleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenantAlertRuleDefinition"] = Field(alias="@odata.type",)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	definitionTemplate: Optional[ManagedTenantsAlertRuleDefinitionTemplate] = Field(alias="definitionTemplate", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	alertRules: Optional[list[ManagedTenantsManagedTenantAlertRule]] = Field(alias="alertRules", default=None,)

from .managed_tenants_alert_rule_definition_template import ManagedTenantsAlertRuleDefinitionTemplate
from .managed_tenants_managed_tenant_alert_rule import ManagedTenantsManagedTenantAlertRule
