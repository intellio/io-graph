from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BaseItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	eTag: Optional[str] = Field(default=None,alias="eTag",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	createdByUser: Optional[User] = Field(default=None,alias="createdByUser",)
	lastModifiedByUser: Optional[User] = Field(default=None,alias="lastModifiedByUser",)

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
			if mapping_key == "#microsoft.graph.baseSitePage":
				from .base_site_page import BaseSitePage
				return BaseSitePage.model_validate(data)
			if mapping_key == "#microsoft.graph.sitePage":
				from .site_page import SitePage
				return SitePage.model_validate(data)
			if mapping_key == "#microsoft.graph.drive":
				from .drive import Drive
				return Drive.model_validate(data)
			if mapping_key == "#microsoft.graph.driveItem":
				from .drive_item import DriveItem
				return DriveItem.model_validate(data)
			if mapping_key == "#microsoft.graph.list":
				from .list import List
				return List.model_validate(data)
			if mapping_key == "#microsoft.graph.listItem":
				from .list_item import ListItem
				return ListItem.model_validate(data)
			if mapping_key == "#microsoft.graph.recycleBin":
				from .recycle_bin import RecycleBin
				return RecycleBin.model_validate(data)
			if mapping_key == "#microsoft.graph.recycleBinItem":
				from .recycle_bin_item import RecycleBinItem
				return RecycleBinItem.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedDriveItem":
				from .shared_drive_item import SharedDriveItem
				return SharedDriveItem.model_validate(data)
			if mapping_key == "#microsoft.graph.site":
				from .site import Site
				return Site.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User

