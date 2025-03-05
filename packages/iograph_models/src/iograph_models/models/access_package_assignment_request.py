from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	answers: SerializeAsAny[Optional[list[AccessPackageAnswer]]] = Field(alias="answers",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(alias="customExtensionCalloutInstances",default=None,)
	requestType: Optional[str | AccessPackageRequestType] = Field(alias="requestType",default=None,)
	schedule: Optional[EntitlementManagementSchedule] = Field(alias="schedule",default=None,)
	state: Optional[str | AccessPackageRequestState] = Field(alias="state",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage",default=None,)
	assignment: Optional[AccessPackageAssignment] = Field(alias="assignment",default=None,)
	requestor: Optional[AccessPackageSubject] = Field(alias="requestor",default=None,)

from .access_package_answer import AccessPackageAnswer
from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .access_package_request_type import AccessPackageRequestType
from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_request_state import AccessPackageRequestState
from .access_package import AccessPackage
from .access_package_assignment import AccessPackageAssignment
from .access_package_subject import AccessPackageSubject

