from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftManagedDesktop(BaseModel):
	managedType: Optional[MicrosoftManagedDesktopType | str] = Field(alias="managedType", default=None,)
	profile: Optional[str] = Field(alias="profile", default=None,)
	type: Optional[MicrosoftManagedDesktopType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .microsoft_managed_desktop_type import MicrosoftManagedDesktopType
from .microsoft_managed_desktop_type import MicrosoftManagedDesktopType

