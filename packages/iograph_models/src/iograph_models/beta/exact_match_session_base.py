from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExactMatchSessionBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime",default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime",default=None,)
	error: Optional[ClassificationError] = Field(alias="error",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	dataStoreId: Optional[str] = Field(alias="dataStoreId",default=None,)
	processingCompletionDateTime: Optional[datetime] = Field(alias="processingCompletionDateTime",default=None,)
	remainingBlockCount: Optional[int] = Field(alias="remainingBlockCount",default=None,)
	remainingJobCount: Optional[int] = Field(alias="remainingJobCount",default=None,)
	state: Optional[str] = Field(alias="state",default=None,)
	totalBlockCount: Optional[int] = Field(alias="totalBlockCount",default=None,)
	totalJobCount: Optional[int] = Field(alias="totalJobCount",default=None,)
	uploadCompletionDateTime: Optional[datetime] = Field(alias="uploadCompletionDateTime",default=None,)

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
			if mapping_key == "#microsoft.graph.exactMatchSession":
				from .exact_match_session import ExactMatchSession
				return ExactMatchSession.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .classification_error import ClassificationError

