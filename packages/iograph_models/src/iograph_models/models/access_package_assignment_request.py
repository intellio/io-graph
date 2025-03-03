from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	answers: Optional[list[AccessPackageAnswer]] = Field(default=None,alias="answers",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(default=None,alias="customExtensionCalloutInstances",)
	requestType: Optional[AccessPackageRequestType] = Field(default=None,alias="requestType",)
	schedule: Optional[EntitlementManagementSchedule] = Field(default=None,alias="schedule",)
	state: Optional[AccessPackageRequestState] = Field(default=None,alias="state",)
	status: Optional[str] = Field(default=None,alias="status",)
	accessPackage: Optional[AccessPackage] = Field(default=None,alias="accessPackage",)
	assignment: Optional[AccessPackageAssignment] = Field(default=None,alias="assignment",)
	requestor: Optional[AccessPackageSubject] = Field(default=None,alias="requestor",)

from .access_package_answer import AccessPackageAnswer
from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .access_package_request_type import AccessPackageRequestType
from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_request_state import AccessPackageRequestState
from .access_package import AccessPackage
from .access_package_assignment import AccessPackageAssignment
from .access_package_subject import AccessPackageSubject

