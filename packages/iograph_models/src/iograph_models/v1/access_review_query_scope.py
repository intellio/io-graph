from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AccessReviewQueryScope(BaseModel):
	odata_type: Literal["#microsoft.graph.accessReviewQueryScope"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewQueryScope")
	query: Optional[str] = Field(alias="query", default=None,)
	queryRoot: Optional[str] = Field(alias="queryRoot", default=None,)
	queryType: Optional[str] = Field(alias="queryType", default=None,)

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
			if mapping_key == "#microsoft.graph.accessReviewInactiveUsersQueryScope":
				from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
				return AccessReviewInactiveUsersQueryScope.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

