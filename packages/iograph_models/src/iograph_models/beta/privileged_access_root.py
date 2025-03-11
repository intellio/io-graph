from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	group: Optional[PrivilegedAccessGroup] = Field(alias="group",default=None,)

from .privileged_access_group import PrivilegedAccessGroup

