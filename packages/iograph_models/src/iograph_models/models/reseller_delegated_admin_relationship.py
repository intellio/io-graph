from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ResellerDelegatedAdminRelationship(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessDetails: Optional[DelegatedAdminAccessDetails] = Field(default=None,alias="accessDetails",)
	activatedDateTime: Optional[datetime] = Field(default=None,alias="activatedDateTime",)
	autoExtendDuration: Optional[str] = Field(default=None,alias="autoExtendDuration",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customer: Optional[DelegatedAdminRelationshipCustomerParticipant] = Field(default=None,alias="customer",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	duration: Optional[str] = Field(default=None,alias="duration",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[DelegatedAdminRelationshipStatus] = Field(default=None,alias="status",)
	accessAssignments: Optional[list[DelegatedAdminAccessAssignment]] = Field(default=None,alias="accessAssignments",)
	operations: Optional[list[DelegatedAdminRelationshipOperation]] = Field(default=None,alias="operations",)
	requests: Optional[list[DelegatedAdminRelationshipRequest]] = Field(default=None,alias="requests",)
	indirectProviderTenantId: Optional[str] = Field(default=None,alias="indirectProviderTenantId",)
	isPartnerConsentPending: Optional[bool] = Field(default=None,alias="isPartnerConsentPending",)

from .delegated_admin_access_details import DelegatedAdminAccessDetails
from .delegated_admin_relationship_customer_participant import DelegatedAdminRelationshipCustomerParticipant
from .delegated_admin_relationship_status import DelegatedAdminRelationshipStatus
from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest

