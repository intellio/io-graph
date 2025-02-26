from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftManagedDesktop(BaseModel):
	managedType: Optional[MicrosoftManagedDesktopType] = Field(default=None,alias="managedType",)
	profile: Optional[str] = Field(default=None,alias="profile",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .microsoft_managed_desktop_type import MicrosoftManagedDesktopType

