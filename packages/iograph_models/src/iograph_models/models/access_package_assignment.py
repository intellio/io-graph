from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(default=None,alias="customExtensionCalloutInstances",)
	expiredDateTime: Optional[datetime] = Field(default=None,alias="expiredDateTime",)
	schedule: Optional[EntitlementManagementSchedule] = Field(default=None,alias="schedule",)
	state: Optional[AccessPackageAssignmentState] = Field(default=None,alias="state",)
	status: Optional[str] = Field(default=None,alias="status",)
	accessPackage: Optional[AccessPackage] = Field(default=None,alias="accessPackage",)
	assignmentPolicy: Optional[AccessPackageAssignmentPolicy] = Field(default=None,alias="assignmentPolicy",)
	target: Optional[AccessPackageSubject] = Field(default=None,alias="target",)

from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_assignment_state import AccessPackageAssignmentState
from .access_package import AccessPackage
from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_subject import AccessPackageSubject

