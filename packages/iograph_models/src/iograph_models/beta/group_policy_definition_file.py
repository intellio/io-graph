from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyDefinitionFile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)
	languageCodes: Optional[list[str]] = Field(alias="languageCodes",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	policyType: Optional[GroupPolicyType | str] = Field(alias="policyType",default=None,)
	revision: Optional[str] = Field(alias="revision",default=None,)
	targetNamespace: Optional[str] = Field(alias="targetNamespace",default=None,)
	targetPrefix: Optional[str] = Field(alias="targetPrefix",default=None,)
	definitions: Optional[list[GroupPolicyDefinition]] = Field(alias="definitions",default=None,)

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
			if mapping_key == "#microsoft.graph.groupPolicyUploadedDefinitionFile":
				from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
				return GroupPolicyUploadedDefinitionFile.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .group_policy_type import GroupPolicyType
from .group_policy_definition import GroupPolicyDefinition

