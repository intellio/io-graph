from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	allowedTargetScope: Optional[AllowedTargetScope | str] = Field(alias="allowedTargetScope", default=None,)
	automaticRequestSettings: Optional[AccessPackageAutomaticRequestSettings] = Field(alias="automaticRequestSettings", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	expiration: Optional[ExpirationPattern] = Field(alias="expiration", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	requestApprovalSettings: Optional[AccessPackageAssignmentApprovalSettings] = Field(alias="requestApprovalSettings", default=None,)
	requestorSettings: Optional[AccessPackageAssignmentRequestorSettings] = Field(alias="requestorSettings", default=None,)
	reviewSettings: Optional[AccessPackageAssignmentReviewSettings] = Field(alias="reviewSettings", default=None,)
	specificAllowedTargets: Optional[list[Annotated[Union[AttributeRuleMembers, ConnectedOrganizationMembers, ExternalSponsors, GroupMembers, InternalSponsors, RequestorManager, SingleServicePrincipal, SingleUser, TargetApplicationOwners, TargetManager, TargetUserSponsors, IdentityGovernanceGroupBasedSubjectSet, IdentityGovernanceRuleBasedSubjectSet],Field(discriminator="odata_type")]]] = Field(alias="specificAllowedTargets", default=None,)
	accessPackage: Optional[AccessPackage] = Field(alias="accessPackage", default=None,)
	catalog: Optional[AccessPackageCatalog] = Field(alias="catalog", default=None,)
	customExtensionStageSettings: Optional[list[CustomExtensionStageSetting]] = Field(alias="customExtensionStageSettings", default=None,)
	questions: Optional[list[Annotated[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion],Field(discriminator="odata_type")]]] = Field(alias="questions", default=None,)

from .allowed_target_scope import AllowedTargetScope
from .access_package_automatic_request_settings import AccessPackageAutomaticRequestSettings
from .expiration_pattern import ExpirationPattern
from .access_package_assignment_approval_settings import AccessPackageAssignmentApprovalSettings
from .access_package_assignment_requestor_settings import AccessPackageAssignmentRequestorSettings
from .access_package_assignment_review_settings import AccessPackageAssignmentReviewSettings
from .attribute_rule_members import AttributeRuleMembers
from .connected_organization_members import ConnectedOrganizationMembers
from .external_sponsors import ExternalSponsors
from .group_members import GroupMembers
from .internal_sponsors import InternalSponsors
from .requestor_manager import RequestorManager
from .single_service_principal import SingleServicePrincipal
from .single_user import SingleUser
from .target_application_owners import TargetApplicationOwners
from .target_manager import TargetManager
from .target_user_sponsors import TargetUserSponsors
from .identity_governance_group_based_subject_set import IdentityGovernanceGroupBasedSubjectSet
from .identity_governance_rule_based_subject_set import IdentityGovernanceRuleBasedSubjectSet
from .access_package import AccessPackage
from .access_package_catalog import AccessPackageCatalog
from .custom_extension_stage_setting import CustomExtensionStageSetting
from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion

