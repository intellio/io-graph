from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesCatalogContent(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	catalogEntry: SerializeAsAny[Optional[WindowsUpdatesCatalogEntry]] = Field(alias="catalogEntry",default=None,)

from .windows_updates_catalog_entry import WindowsUpdatesCatalogEntry

