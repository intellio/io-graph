from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class LabelDetails(BaseModel):
	color: Optional[str] = Field(alias="color", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parent: Optional[Union[LabelDetails]] = Field(alias="parent", default=None,discriminator="odata_type", )
	sensitivity: Optional[int] = Field(alias="sensitivity", default=None,)
	tooltip: Optional[str] = Field(alias="tooltip", default=None,)
	odata_type: Literal["#microsoft.graph.labelDetails"] = Field(alias="@odata.type", default="#microsoft.graph.labelDetails")


