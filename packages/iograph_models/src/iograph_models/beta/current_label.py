from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CurrentLabel(BaseModel):
	applicationMode: Optional[ApplicationMode | str] = Field(alias="applicationMode", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .application_mode import ApplicationMode

