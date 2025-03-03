from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageAssignmentPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedTargetScope: Optional[AllowedTargetScope] = Field(default=None,alias="allowedTargetScope",)
	automaticRequestSettings: Optional[AccessPackageAutomaticRequestSettings] = Field(default=None,alias="automaticRequestSettings",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	expiration: Optional[ExpirationPattern] = Field(default=None,alias="expiration",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	requestApprovalSettings: Optional[AccessPackageAssignmentApprovalSettings] = Field(default=None,alias="requestApprovalSettings",)
	requestorSettings: Optional[AccessPackageAssignmentRequestorSettings] = Field(default=None,alias="requestorSettings",)
	reviewSettings: Optional[AccessPackageAssignmentReviewSettings] = Field(default=None,alias="reviewSettings",)
	specificAllowedTargets: Optional[list[SubjectSet]] = Field(default=None,alias="specificAllowedTargets",)
	accessPackage: Optional[AccessPackage] = Field(default=None,alias="accessPackage",)
	catalog: Optional[AccessPackageCatalog] = Field(default=None,alias="catalog",)
	customExtensionStageSettings: Optional[list[CustomExtensionStageSetting]] = Field(default=None,alias="customExtensionStageSettings",)
	questions: Optional[list[AccessPackageQuestion]] = Field(default=None,alias="questions",)

from .allowed_target_scope import AllowedTargetScope
from .access_package_automatic_request_settings import AccessPackageAutomaticRequestSettings
from .expiration_pattern import ExpirationPattern
from .access_package_assignment_approval_settings import AccessPackageAssignmentApprovalSettings
from .access_package_assignment_requestor_settings import AccessPackageAssignmentRequestorSettings
from .access_package_assignment_review_settings import AccessPackageAssignmentReviewSettings
from .subject_set import SubjectSet
from .access_package import AccessPackage
from .access_package_catalog import AccessPackageCatalog
from .custom_extension_stage_setting import CustomExtensionStageSetting
from .access_package_question import AccessPackageQuestion

