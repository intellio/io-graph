from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharePointIdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="application",)
	device: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="device",)
	user: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	group: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="group",)
	siteGroup: Optional[SharePointIdentity] = Field(default=None,alias="siteGroup",)
	siteUser: Optional[SharePointIdentity] = Field(default=None,alias="siteUser",)

from .identity import Identity
from .identity import Identity
from .identity import Identity
from .identity import Identity
from .share_point_identity import SharePointIdentity
from .share_point_identity import SharePointIdentity

