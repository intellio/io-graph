from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LockPostRequest(BaseModel):
	lockState: Optional[str | SiteLockState] = Field(alias="lockState",default=None,)

from .site_lock_state import SiteLockState

