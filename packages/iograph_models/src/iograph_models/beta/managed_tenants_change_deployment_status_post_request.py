from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Managed_tenants_change_deployment_statusPostRequest(BaseModel):
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	managementTemplateStepId: Optional[str] = Field(alias="managementTemplateStepId", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)


