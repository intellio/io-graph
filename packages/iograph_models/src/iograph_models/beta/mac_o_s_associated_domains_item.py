from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSAssociatedDomainsItem(BaseModel):
	applicationIdentifier: Optional[str] = Field(alias="applicationIdentifier", default=None,)
	directDownloadsEnabled: Optional[bool] = Field(alias="directDownloadsEnabled", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


