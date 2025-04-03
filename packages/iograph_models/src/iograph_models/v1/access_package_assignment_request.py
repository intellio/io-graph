from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageAssignmentRequest"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageAssignmentRequest")
	answers: Optional[list[Annotated[Union[AccessPackageAnswerString],Field(discriminator="odata_type")]]] = Field(alias="answers", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(alias="customExtensionCalloutInstances", default=None,)
	requestType: Optional[AccessPackageRequestType | str] = Field(alias="requestType", default=None,)
	schedule: Optional[EntitlementManagementSchedule] = Field(alias="schedule", default=None,)
	state: Optional[AccessPackageRequestState | str] = Field(alias="state", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage", default=None,)
	assignment: Optional[AccessPackageAssignment] = Field(alias="assignment", default=None,)
	requestor: Optional[AccessPackageSubject] = Field(alias="requestor", default=None,)

from .access_package_answer_string import AccessPackageAnswerString
from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .access_package_request_type import AccessPackageRequestType
from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_request_state import AccessPackageRequestState
from .access_package import AccessPackage
from .access_package_assignment import AccessPackageAssignment
from .access_package_subject import AccessPackageSubject
