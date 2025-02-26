from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ComplianceManagementPartner(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	androidEnrollmentAssignments: list[ComplianceManagementPartnerAssignment] = Field(alias="androidEnrollmentAssignments",)
	androidOnboarded: Optional[bool] = Field(default=None,alias="androidOnboarded",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	iosEnrollmentAssignments: list[ComplianceManagementPartnerAssignment] = Field(alias="iosEnrollmentAssignments",)
	iosOnboarded: Optional[bool] = Field(default=None,alias="iosOnboarded",)
	lastHeartbeatDateTime: Optional[datetime] = Field(default=None,alias="lastHeartbeatDateTime",)
	macOsEnrollmentAssignments: list[ComplianceManagementPartnerAssignment] = Field(alias="macOsEnrollmentAssignments",)
	macOsOnboarded: Optional[bool] = Field(default=None,alias="macOsOnboarded",)
	partnerState: Optional[DeviceManagementPartnerTenantState] = Field(default=None,alias="partnerState",)

from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState

