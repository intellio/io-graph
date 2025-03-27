from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Assigned_access_multi_mode_profilesPostRequest(BaseModel):
	assignedAccessMultiModeProfiles: Optional[list[WindowsAssignedAccessProfile]] = Field(alias="assignedAccessMultiModeProfiles", default=None,)

from .windows_assigned_access_profile import WindowsAssignedAccessProfile

