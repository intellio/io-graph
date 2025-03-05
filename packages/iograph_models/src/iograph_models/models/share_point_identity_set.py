from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharePointIdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(alias="application",default=None,)
	device: SerializeAsAny[Optional[Identity]] = Field(alias="device",default=None,)
	user: SerializeAsAny[Optional[Identity]] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	group: SerializeAsAny[Optional[Identity]] = Field(alias="group",default=None,)
	siteGroup: Optional[SharePointIdentity] = Field(alias="siteGroup",default=None,)
	siteUser: Optional[SharePointIdentity] = Field(alias="siteUser",default=None,)

from .identity import Identity
from .identity import Identity
from .identity import Identity
from .identity import Identity
from .share_point_identity import SharePointIdentity
from .share_point_identity import SharePointIdentity

