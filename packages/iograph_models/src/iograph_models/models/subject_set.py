from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectSet(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.attributeRuleMembers":
				from .attribute_rule_members import AttributeRuleMembers
				return AttributeRuleMembers.model_validate(data)
			if mapping_key == "#microsoft.graph.connectedOrganizationMembers":
				from .connected_organization_members import ConnectedOrganizationMembers
				return ConnectedOrganizationMembers.model_validate(data)
			if mapping_key == "#microsoft.graph.externalSponsors":
				from .external_sponsors import ExternalSponsors
				return ExternalSponsors.model_validate(data)
			if mapping_key == "#microsoft.graph.groupMembers":
				from .group_members import GroupMembers
				return GroupMembers.model_validate(data)
			if mapping_key == "#microsoft.graph.internalSponsors":
				from .internal_sponsors import InternalSponsors
				return InternalSponsors.model_validate(data)
			if mapping_key == "#microsoft.graph.requestorManager":
				from .requestor_manager import RequestorManager
				return RequestorManager.model_validate(data)
			if mapping_key == "#microsoft.graph.singleServicePrincipal":
				from .single_service_principal import SingleServicePrincipal
				return SingleServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.singleUser":
				from .single_user import SingleUser
				return SingleUser.model_validate(data)
			if mapping_key == "#microsoft.graph.targetApplicationOwners":
				from .target_application_owners import TargetApplicationOwners
				return TargetApplicationOwners.model_validate(data)
			if mapping_key == "#microsoft.graph.targetManager":
				from .target_manager import TargetManager
				return TargetManager.model_validate(data)
			if mapping_key == "#microsoft.graph.targetUserSponsors":
				from .target_user_sponsors import TargetUserSponsors
				return TargetUserSponsors.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.groupBasedSubjectSet":
				from .identity_governance_group_based_subject_set import IdentityGovernanceGroupBasedSubjectSet
				return IdentityGovernanceGroupBasedSubjectSet.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.ruleBasedSubjectSet":
				from .identity_governance_rule_based_subject_set import IdentityGovernanceRuleBasedSubjectSet
				return IdentityGovernanceRuleBasedSubjectSet.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


