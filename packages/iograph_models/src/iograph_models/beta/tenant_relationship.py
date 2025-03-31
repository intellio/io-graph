from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class TenantRelationship(BaseModel):
	delegatedAdminCustomers: Optional[list[DelegatedAdminCustomer]] = Field(alias="delegatedAdminCustomers", default=None,)
	delegatedAdminRelationships: Optional[list[Annotated[Union[ResellerDelegatedAdminRelationship],Field(discriminator="odata_type")]]] = Field(alias="delegatedAdminRelationships", default=None,)
	managedTenants: Optional[ManagedTenantsManagedTenant] = Field(alias="managedTenants", default=None,)
	multiTenantOrganization: Optional[MultiTenantOrganization] = Field(alias="multiTenantOrganization", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .delegated_admin_customer import DelegatedAdminCustomer
from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
from .managed_tenants_managed_tenant import ManagedTenantsManagedTenant
from .multi_tenant_organization import MultiTenantOrganization
