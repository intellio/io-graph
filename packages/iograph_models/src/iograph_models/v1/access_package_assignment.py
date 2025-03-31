from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageAssignment"] = Field(alias="@odata.type",)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(alias="customExtensionCalloutInstances", default=None,)
	expiredDateTime: Optional[datetime] = Field(alias="expiredDateTime", default=None,)
	schedule: Optional[EntitlementManagementSchedule] = Field(alias="schedule", default=None,)
	state: Optional[AccessPackageAssignmentState | str] = Field(alias="state", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage", default=None,)
	assignmentPolicy: Optional[AccessPackageAssignmentPolicy] = Field(alias="assignmentPolicy", default=None,)
	target: Optional[AccessPackageSubject] = Field(alias="target", default=None,)

from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_assignment_state import AccessPackageAssignmentState
from .access_package import AccessPackage
from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_subject import AccessPackageSubject
