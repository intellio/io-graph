from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIndicator(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	source: Optional[SecurityIndicatorSource | str] = Field(alias="source",default=None,)
	artifact: SerializeAsAny[Optional[SecurityArtifact]] = Field(alias="artifact",default=None,)

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
			if mapping_key == "#microsoft.graph.security.articleIndicator":
				from .security_article_indicator import SecurityArticleIndicator
				return SecurityArticleIndicator.model_validate(data)
			if mapping_key == "#microsoft.graph.security.intelligenceProfileIndicator":
				from .security_intelligence_profile_indicator import SecurityIntelligenceProfileIndicator
				return SecurityIntelligenceProfileIndicator.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_indicator_source import SecurityIndicatorSource
from .security_artifact import SecurityArtifact

