from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProfileCardProperty(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.profileCardProperty"] = Field(alias="@odata.type", default="#microsoft.graph.profileCardProperty")
	annotations: Optional[list[ProfileCardAnnotation]] = Field(alias="annotations", default=None,)
	directoryPropertyName: Optional[str] = Field(alias="directoryPropertyName", default=None,)

from .profile_card_annotation import ProfileCardAnnotation
