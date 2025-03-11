from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingViewpoint(BaseModel):
	defaultSharingLink: Optional[DefaultSharingLink] = Field(alias="defaultSharingLink",default=None,)
	sharingAbilities: Optional[SharePointSharingAbilities] = Field(alias="sharingAbilities",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .default_sharing_link import DefaultSharingLink
from .share_point_sharing_abilities import SharePointSharingAbilities

