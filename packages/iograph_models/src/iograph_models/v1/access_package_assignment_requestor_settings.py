from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequestorSettings(BaseModel):
	allowCustomAssignmentSchedule: Optional[bool] = Field(alias="allowCustomAssignmentSchedule", default=None,)
	enableOnBehalfRequestorsToAddAccess: Optional[bool] = Field(alias="enableOnBehalfRequestorsToAddAccess", default=None,)
	enableOnBehalfRequestorsToRemoveAccess: Optional[bool] = Field(alias="enableOnBehalfRequestorsToRemoveAccess", default=None,)
	enableOnBehalfRequestorsToUpdateAccess: Optional[bool] = Field(alias="enableOnBehalfRequestorsToUpdateAccess", default=None,)
	enableTargetsToSelfAddAccess: Optional[bool] = Field(alias="enableTargetsToSelfAddAccess", default=None,)
	enableTargetsToSelfRemoveAccess: Optional[bool] = Field(alias="enableTargetsToSelfRemoveAccess", default=None,)
	enableTargetsToSelfUpdateAccess: Optional[bool] = Field(alias="enableTargetsToSelfUpdateAccess", default=None,)
	onBehalfRequestors: Optional[list[Annotated[Union[AttributeRuleMembers, ConnectedOrganizationMembers, ExternalSponsors, GroupMembers, InternalSponsors, RequestorManager, SingleServicePrincipal, SingleUser, TargetApplicationOwners, TargetManager, TargetUserSponsors, IdentityGovernanceGroupBasedSubjectSet, IdentityGovernanceRuleBasedSubjectSet],Field(discriminator="odata_type")]]] = Field(alias="onBehalfRequestors", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
