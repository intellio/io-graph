from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class Location(BaseModel):
	address: Optional[PhysicalAddress] = Field(alias="address",default=None,)
	coordinates: Optional[OutlookGeoCoordinates] = Field(alias="coordinates",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	locationEmailAddress: Optional[str] = Field(alias="locationEmailAddress",default=None,)
	locationType: Optional[str | LocationType] = Field(alias="locationType",default=None,)
	locationUri: Optional[str] = Field(alias="locationUri",default=None,)
	uniqueId: Optional[str] = Field(alias="uniqueId",default=None,)
	uniqueIdType: Optional[str | LocationUniqueIdType] = Field(alias="uniqueIdType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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

