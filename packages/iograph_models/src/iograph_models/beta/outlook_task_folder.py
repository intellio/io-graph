from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutlookTaskFolder(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	isDefaultFolder: Optional[bool] = Field(alias="isDefaultFolder", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parentGroupKey: Optional[UUID] = Field(alias="parentGroupKey", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)
	tasks: Optional[list[OutlookTask]] = Field(alias="tasks", default=None,)

from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from .outlook_task import OutlookTask

