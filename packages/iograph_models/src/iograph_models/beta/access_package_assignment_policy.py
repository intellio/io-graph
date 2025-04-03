from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageAssignmentPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageAssignmentPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageAssignmentPolicy")
	accessPackageId: Optional[str] = Field(alias="accessPackageId", default=None,)
	accessPackageNotificationSettings: Optional[AccessPackageNotificationSettings] = Field(alias="accessPackageNotificationSettings", default=None,)
	accessReviewSettings: Optional[AssignmentReviewSettings] = Field(alias="accessReviewSettings", default=None,)
	canExtend: Optional[bool] = Field(alias="canExtend", default=None,)
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	modifiedBy: Optional[str] = Field(alias="modifiedBy", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	questions: Optional[list[Annotated[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion],Field(discriminator="odata_type")]]] = Field(alias="questions", default=None,)
	requestApprovalSettings: Optional[ApprovalSettings] = Field(alias="requestApprovalSettings", default=None,)
	requestorSettings: Optional[RequestorSettings] = Field(alias="requestorSettings", default=None,)
	verifiableCredentialSettings: Optional[VerifiableCredentialSettings] = Field(alias="verifiableCredentialSettings", default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage", default=None,)
	accessPackageCatalog: Optional[AccessPackageCatalog] = Field(alias="accessPackageCatalog", default=None,)
	customExtensionHandlers: Optional[list[CustomExtensionHandler]] = Field(alias="customExtensionHandlers", default=None,)
	customExtensionStageSettings: Optional[list[CustomExtensionStageSetting]] = Field(alias="customExtensionStageSettings", default=None,)

from .access_package_notification_settings import AccessPackageNotificationSettings
from .assignment_review_settings import AssignmentReviewSettings
from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion
from .approval_settings import ApprovalSettings
from .requestor_settings import RequestorSettings
from .verifiable_credential_settings import VerifiableCredentialSettings
from .access_package import AccessPackage
from .access_package_catalog import AccessPackageCatalog
from .custom_extension_handler import CustomExtensionHandler
from .custom_extension_stage_setting import CustomExtensionStageSetting
