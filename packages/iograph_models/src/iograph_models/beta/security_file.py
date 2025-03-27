from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	dateTime: Optional[datetime] = Field(alias="dateTime", default=None,)
	extension: Optional[str] = Field(alias="extension", default=None,)
	extractedTextContent: Optional[str] = Field(alias="extractedTextContent", default=None,)
	mediaType: Optional[str] = Field(alias="mediaType", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	otherProperties: Optional[SecurityStringValueDictionary] = Field(alias="otherProperties", default=None,)
	processingStatus: Optional[SecurityFileProcessingStatus | str] = Field(alias="processingStatus", default=None,)
	senderOrAuthors: Optional[list[str]] = Field(alias="senderOrAuthors", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	sourceType: Optional[SecuritySourceType | str] = Field(alias="sourceType", default=None,)
	subjectTitle: Optional[str] = Field(alias="subjectTitle", default=None,)

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
			if mapping_key == "#microsoft.graph.security.ediscoveryFile":
				from .security_ediscovery_file import SecurityEdiscoveryFile
				return SecurityEdiscoveryFile.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_string_value_dictionary import SecurityStringValueDictionary
from .security_file_processing_status import SecurityFileProcessingStatus
from .security_source_type import SecuritySourceType

