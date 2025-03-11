from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidPermissionAction(BaseModel):
	action: Optional[AndroidPermissionActionType | str] = Field(alias="action",default=None,)
	permission: Optional[str] = Field(alias="permission",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .android_permission_action_type import AndroidPermissionActionType

