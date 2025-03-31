from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class UploadSession(BaseModel):
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	nextExpectedRanges: Optional[list[str]] = Field(alias="nextExpectedRanges", default=None,)
	uploadUrl: Optional[str] = Field(alias="uploadUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.engagementUploadSession":
				from .engagement_upload_session import EngagementUploadSession
				return EngagementUploadSession.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

