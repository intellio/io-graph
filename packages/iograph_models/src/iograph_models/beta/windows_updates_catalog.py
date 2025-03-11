from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesCatalog(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	entries: SerializeAsAny[Optional[list[WindowsUpdatesCatalogEntry]]] = Field(alias="entries",default=None,)

from .windows_updates_catalog_entry import WindowsUpdatesCatalogEntry

