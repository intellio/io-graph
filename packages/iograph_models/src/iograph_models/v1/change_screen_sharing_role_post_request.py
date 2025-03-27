from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Change_screen_sharing_rolePostRequest(BaseModel):
	role: Optional[ScreenSharingRole | str] = Field(alias="role", default=None,)

from .screen_sharing_role import ScreenSharingRole

