from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class Location(BaseModel):
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	coordinates: Optional[OutlookGeoCoordinates] = Field(default=None,alias="coordinates",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	locationEmailAddress: Optional[str] = Field(default=None,alias="locationEmailAddress",)
	locationType: Optional[LocationType] = Field(default=None,alias="locationType",)
	locationUri: Optional[str] = Field(default=None,alias="locationUri",)
	uniqueId: Optional[str] = Field(default=None,alias="uniqueId",)
	uniqueIdType: Optional[LocationUniqueIdType] = Field(default=None,alias="uniqueIdType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.locationConstraintItem":
				from .location_constraint_item import LocationConstraintItem
				return LocationConstraintItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .location_type import LocationType
from .location_unique_id_type import LocationUniqueIdType

