from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class SearchSearchAnswer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[SearchIdentitySet] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)

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
			if mapping_key == "#microsoft.graph.search.acronym":
				from .search_acronym import SearchAcronym
				return SearchAcronym.model_validate(data)
			if mapping_key == "#microsoft.graph.search.bookmark":
				from .search_bookmark import SearchBookmark
				return SearchBookmark.model_validate(data)
			if mapping_key == "#microsoft.graph.search.qna":
				from .search_qna import SearchQna
				return SearchQna.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .search_identity_set import SearchIdentitySet
