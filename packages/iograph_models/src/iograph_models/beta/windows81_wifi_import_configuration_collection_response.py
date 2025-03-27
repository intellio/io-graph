from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows81WifiImportConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows81WifiImportConfiguration]] = Field(alias="value", default=None,)

from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration

