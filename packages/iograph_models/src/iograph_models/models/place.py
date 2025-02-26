from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class Place(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	geoCoordinates: Optional[OutlookGeoCoordinates] = Field(default=None,alias="geoCoordinates",)
	phone: Optional[str] = Field(default=None,alias="phone",)

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
			if mapping_key == "#microsoft.graph.room":
				from .room import Room
				return Room.model_validate(data)
			if mapping_key == "#microsoft.graph.roomList":
				from .room_list import RoomList
				return RoomList.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates

