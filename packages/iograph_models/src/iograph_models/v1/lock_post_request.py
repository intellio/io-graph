from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LockPostRequest(BaseModel):
	lockState: Optional[SiteLockState | str] = Field(alias="lockState", default=None,)

from .site_lock_state import SiteLockState
