from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class SecurityFilePlanDescriptorTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

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
			if mapping_key == "#microsoft.graph.security.authorityTemplate":
				from .security_authority_template import SecurityAuthorityTemplate
				return SecurityAuthorityTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.categoryTemplate":
				from .security_category_template import SecurityCategoryTemplate
				return SecurityCategoryTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.citationTemplate":
				from .security_citation_template import SecurityCitationTemplate
				return SecurityCitationTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.departmentTemplate":
				from .security_department_template import SecurityDepartmentTemplate
				return SecurityDepartmentTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanReferenceTemplate":
				from .security_file_plan_reference_template import SecurityFilePlanReferenceTemplate
				return SecurityFilePlanReferenceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.subcategoryTemplate":
				from .security_subcategory_template import SecuritySubcategoryTemplate
				return SecuritySubcategoryTemplate.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
