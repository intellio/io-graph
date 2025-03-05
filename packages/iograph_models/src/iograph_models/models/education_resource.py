from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationResource(BaseModel):
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
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
			if mapping_key == "#microsoft.graph.educationChannelResource":
				from .education_channel_resource import EducationChannelResource
				return EducationChannelResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationExcelResource":
				from .education_excel_resource import EducationExcelResource
				return EducationExcelResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationExternalResource":
				from .education_external_resource import EducationExternalResource
				return EducationExternalResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationFileResource":
				from .education_file_resource import EducationFileResource
				return EducationFileResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationLinkedAssignmentResource":
				from .education_linked_assignment_resource import EducationLinkedAssignmentResource
				return EducationLinkedAssignmentResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationLinkResource":
				from .education_link_resource import EducationLinkResource
				return EducationLinkResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationMediaResource":
				from .education_media_resource import EducationMediaResource
				return EducationMediaResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationPowerPointResource":
				from .education_power_point_resource import EducationPowerPointResource
				return EducationPowerPointResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationTeamsAppResource":
				from .education_teams_app_resource import EducationTeamsAppResource
				return EducationTeamsAppResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationWordResource":
				from .education_word_resource import EducationWordResource
				return EducationWordResource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .identity_set import IdentitySet

