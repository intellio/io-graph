from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProfileCardProperty(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	annotations: Optional[list[ProfileCardAnnotation]] = Field(alias="annotations", default=None,)
	directoryPropertyName: Optional[str] = Field(alias="directoryPropertyName", default=None,)

from .profile_card_annotation import ProfileCardAnnotation

