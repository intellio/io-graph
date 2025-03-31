from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EditionUpgradeConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EditionUpgradeConfiguration]] = Field(alias="value", default=None,)

from .edition_upgrade_configuration import EditionUpgradeConfiguration
