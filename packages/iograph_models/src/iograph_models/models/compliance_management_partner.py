from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ComplianceManagementPartner(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	androidEnrollmentAssignments: Optional[list[ComplianceManagementPartnerAssignment]] = Field(alias="androidEnrollmentAssignments",default=None,)
	androidOnboarded: Optional[bool] = Field(alias="androidOnboarded",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	iosEnrollmentAssignments: Optional[list[ComplianceManagementPartnerAssignment]] = Field(alias="iosEnrollmentAssignments",default=None,)
	iosOnboarded: Optional[bool] = Field(alias="iosOnboarded",default=None,)
	lastHeartbeatDateTime: Optional[datetime] = Field(alias="lastHeartbeatDateTime",default=None,)
	macOsEnrollmentAssignments: Optional[list[ComplianceManagementPartnerAssignment]] = Field(alias="macOsEnrollmentAssignments",default=None,)
	macOsOnboarded: Optional[bool] = Field(alias="macOsOnboarded",default=None,)
	partnerState: Optional[DeviceManagementPartnerTenantState | str] = Field(alias="partnerState",default=None,)

from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState

