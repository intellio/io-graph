from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageResourceEnvironmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessPackageResourceEnvironment]] = Field(alias="value", default=None,)

from .access_package_resource_environment import AccessPackageResourceEnvironment
