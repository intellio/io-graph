from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class Place(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	address: Optional[PhysicalAddress] = Field(alias="address",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	geoCoordinates: Optional[OutlookGeoCoordinates] = Field(alias="geoCoordinates",default=None,)
	phone: Optional[str] = Field(alias="phone",default=None,)
	placeId: Optional[str] = Field(alias="placeId",default=None,)

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
			if mapping_key == "#microsoft.graph.workspace":
				from .workspace import Workspace
				return Workspace.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates

