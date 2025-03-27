from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppRelationship(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	sourceDisplayName: Optional[str] = Field(alias="sourceDisplayName", default=None,)
	sourceDisplayVersion: Optional[str] = Field(alias="sourceDisplayVersion", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	sourcePublisherDisplayName: Optional[str] = Field(alias="sourcePublisherDisplayName", default=None,)
	targetDisplayName: Optional[str] = Field(alias="targetDisplayName", default=None,)
	targetDisplayVersion: Optional[str] = Field(alias="targetDisplayVersion", default=None,)
	targetId: Optional[str] = Field(alias="targetId", default=None,)
	targetPublisher: Optional[str] = Field(alias="targetPublisher", default=None,)
	targetPublisherDisplayName: Optional[str] = Field(alias="targetPublisherDisplayName", default=None,)
	targetType: Optional[MobileAppRelationshipType | str] = Field(alias="targetType", default=None,)

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
			if mapping_key == "#microsoft.graph.mobileAppDependency":
				from .mobile_app_dependency import MobileAppDependency
				return MobileAppDependency.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppSupersedence":
				from .mobile_app_supersedence import MobileAppSupersedence
				return MobileAppSupersedence.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mobile_app_relationship_type import MobileAppRelationshipType

