from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ResellerDelegatedAdminRelationship(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessDetails: Optional[DelegatedAdminAccessDetails] = Field(alias="accessDetails",default=None,)
	activatedDateTime: Optional[datetime] = Field(alias="activatedDateTime",default=None,)
	autoExtendDuration: Optional[str] = Field(alias="autoExtendDuration",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customer: Optional[DelegatedAdminRelationshipCustomerParticipant] = Field(alias="customer",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	duration: Optional[str] = Field(alias="duration",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[str | DelegatedAdminRelationshipStatus] = Field(alias="status",default=None,)
	accessAssignments: Optional[list[DelegatedAdminAccessAssignment]] = Field(alias="accessAssignments",default=None,)
	operations: Optional[list[DelegatedAdminRelationshipOperation]] = Field(alias="operations",default=None,)
	requests: Optional[list[DelegatedAdminRelationshipRequest]] = Field(alias="requests",default=None,)
	indirectProviderTenantId: Optional[str] = Field(alias="indirectProviderTenantId",default=None,)
	isPartnerConsentPending: Optional[bool] = Field(alias="isPartnerConsentPending",default=None,)

from .delegated_admin_access_details import DelegatedAdminAccessDetails
from .delegated_admin_relationship_customer_participant import DelegatedAdminRelationshipCustomerParticipant
from .delegated_admin_relationship_status import DelegatedAdminRelationshipStatus
from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest

