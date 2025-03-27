from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Property(BaseModel):
	aliases: Optional[list[str]] = Field(alias="aliases", default=None,)
	isQueryable: Optional[bool] = Field(alias="isQueryable", default=None,)
	isRefinable: Optional[bool] = Field(alias="isRefinable", default=None,)
	isRetrievable: Optional[bool] = Field(alias="isRetrievable", default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable", default=None,)
	labels: Optional[list[Label | str]] = Field(alias="labels", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	type: Optional[PropertyType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .label import Label
from .property_type import PropertyType

