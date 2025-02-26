from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class AgreementFileProperties(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	fileData: Optional[AgreementFileData] = Field(default=None,alias="fileData",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	isMajorVersion: Optional[bool] = Field(default=None,alias="isMajorVersion",)
	language: Optional[str] = Field(default=None,alias="language",)

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
			if mapping_key == "#microsoft.graph.agreementFile":
				from .agreement_file import AgreementFile
				return AgreementFile.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementFileLocalization":
				from .agreement_file_localization import AgreementFileLocalization
				return AgreementFileLocalization.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementFileVersion":
				from .agreement_file_version import AgreementFileVersion
				return AgreementFileVersion.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .agreement_file_data import AgreementFileData

