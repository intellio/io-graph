from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class InformationProtectionLabel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.informationProtectionLabel"] = Field(alias="@odata.type",)
	color: Optional[str] = Field(alias="color", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parent: Optional[Union[LabelDetails]] = Field(alias="parent", default=None,discriminator="odata_type", )
	sensitivity: Optional[int] = Field(alias="sensitivity", default=None,)
	tooltip: Optional[str] = Field(alias="tooltip", default=None,)

from .label_details import LabelDetails
