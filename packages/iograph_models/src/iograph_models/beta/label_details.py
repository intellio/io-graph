from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LabelDetails(BaseModel):
	color: Optional[str] = Field(alias="color",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	isActive: Optional[bool] = Field(alias="isActive",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parent: SerializeAsAny[Optional[ParentLabelDetails]] = Field(alias="parent",default=None,)
	sensitivity: Optional[int] = Field(alias="sensitivity",default=None,)
	tooltip: Optional[str] = Field(alias="tooltip",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .parent_label_details import ParentLabelDetails

