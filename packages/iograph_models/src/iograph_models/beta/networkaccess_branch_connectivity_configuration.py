from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessBranchConnectivityConfiguration(BaseModel):
	branchId: Optional[str] = Field(alias="branchId",default=None,)
	branchName: Optional[str] = Field(alias="branchName",default=None,)
	links: Optional[list[NetworkaccessConnectivityConfigurationLink]] = Field(alias="links",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_connectivity_configuration_link import NetworkaccessConnectivityConfigurationLink

