from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	answers: SerializeAsAny[Optional[list[AccessPackageAnswer]]] = Field(alias="answers",default=None,)
	completedDate: Optional[datetime] = Field(alias="completedDate",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customExtensionCalloutInstances: Optional[list[CustomExtensionCalloutInstance]] = Field(alias="customExtensionCalloutInstances",default=None,)
	customExtensionHandlerInstances: Optional[list[CustomExtensionHandlerInstance]] = Field(alias="customExtensionHandlerInstances",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	history: Optional[list[RequestActivity]] = Field(alias="history",default=None,)
	isValidationOnly: Optional[bool] = Field(alias="isValidationOnly",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	requestState: Optional[str] = Field(alias="requestState",default=None,)
	requestStatus: Optional[str] = Field(alias="requestStatus",default=None,)
	requestType: Optional[str] = Field(alias="requestType",default=None,)
	schedule: Optional[RequestSchedule] = Field(alias="schedule",default=None,)
	verifiedCredentialsData: Optional[list[VerifiedCredentialData]] = Field(alias="verifiedCredentialsData",default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage",default=None,)
	accessPackageAssignment: Optional[AccessPackageAssignment] = Field(alias="accessPackageAssignment",default=None,)
	requestor: Optional[AccessPackageSubject] = Field(alias="requestor",default=None,)

from .access_package_answer import AccessPackageAnswer
from .custom_extension_callout_instance import CustomExtensionCalloutInstance
from .custom_extension_handler_instance import CustomExtensionHandlerInstance
from .request_activity import RequestActivity
from .request_schedule import RequestSchedule
from .verified_credential_data import VerifiedCredentialData
from .access_package import AccessPackage
from .access_package_assignment import AccessPackageAssignment
from .access_package_subject import AccessPackageSubject

