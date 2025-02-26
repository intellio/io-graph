from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TenantRelationship(BaseModel):
	delegatedAdminCustomers: list[DelegatedAdminCustomer] = Field(alias="delegatedAdminCustomers",)
	delegatedAdminRelationships: list[DelegatedAdminRelationship] = Field(alias="delegatedAdminRelationships",)
	multiTenantOrganization: Optional[MultiTenantOrganization] = Field(default=None,alias="multiTenantOrganization",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .delegated_admin_customer import DelegatedAdminCustomer
from .delegated_admin_relationship import DelegatedAdminRelationship
from .multi_tenant_organization import MultiTenantOrganization

