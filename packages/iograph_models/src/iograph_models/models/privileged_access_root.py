from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	group: Optional[PrivilegedAccessGroup] = Field(default=None,alias="group",)

from .privileged_access_group import PrivilegedAccessGroup

