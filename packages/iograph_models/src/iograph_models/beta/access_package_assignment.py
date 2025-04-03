from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageAssignment")
	accessPackageId: Optional[str] = Field(alias="accessPackageId", default=None,)
	assignmentPolicyId: Optional[str] = Field(alias="assignmentPolicyId", default=None,)
	assignmentState: Optional[str] = Field(alias="assignmentState", default=None,)
	assignmentStatus: Optional[str] = Field(alias="assignmentStatus", default=None,)
	catalogId: Optional[str] = Field(alias="catalogId", default=None,)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(alias="customExtensionCalloutInstances", default=None,)
	expiredDateTime: Optional[datetime] = Field(alias="expiredDateTime", default=None,)
	isExtended: Optional[bool] = Field(alias="isExtended", default=None,)
	schedule: Optional[RequestSchedule] = Field(alias="schedule", default=None,)
	targetId: Optional[str] = Field(alias="targetId", default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage", default=None,)
	accessPackageAssignmentPolicy: Optional[AccessPackageAssignmentPolicy] = Field(alias="accessPackageAssignmentPolicy", default=None,)
	accessPackageAssignmentRequests: Optional[list[AccessPackageAssignmentRequest]] = Field(alias="accessPackageAssignmentRequests", default=None,)
	accessPackageAssignmentResourceRoles: Optional[list[AccessPackageAssignmentResourceRole]] = Field(alias="accessPackageAssignmentResourceRoles", default=None,)
	target: Optional[AccessPackageSubject] = Field(alias="target", default=None,)

from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .request_schedule import RequestSchedule
from .access_package import AccessPackage
from .access_package_assignment_policy import AccessPackageAssignmentPolicy
from .access_package_assignment_request import AccessPackageAssignmentRequest
from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
from .access_package_subject import AccessPackageSubject
