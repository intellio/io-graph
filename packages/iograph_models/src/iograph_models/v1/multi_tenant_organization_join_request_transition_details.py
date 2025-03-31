from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MultiTenantOrganizationJoinRequestTransitionDetails(BaseModel):
	desiredMemberState: Optional[MultiTenantOrganizationMemberState | str] = Field(alias="desiredMemberState", default=None,)
	details: Optional[str] = Field(alias="details", default=None,)
	status: Optional[MultiTenantOrganizationMemberProcessingStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
