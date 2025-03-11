from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WslDistributionConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WslDistributionConfiguration]] = Field(alias="value",default=None,)

from .wsl_distribution_configuration import WslDistributionConfiguration

