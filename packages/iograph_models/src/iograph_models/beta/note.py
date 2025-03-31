from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class Note(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.note"] = Field(alias="@odata.type", default="#microsoft.graph.note")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension, PersonExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .item_body import ItemBody
from .file_attachment import FileAttachment
from .item_attachment import ItemAttachment
from .reference_attachment import ReferenceAttachment
from .open_type_extension import OpenTypeExtension
from .person_extension import PersonExtension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
