from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessConnectivity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	webCategories: Optional[list[NetworkaccessWebCategory]] = Field(alias="webCategories",default=None,)
	branches: Optional[list[NetworkaccessBranchSite]] = Field(alias="branches",default=None,)
	remoteNetworks: Optional[list[NetworkaccessRemoteNetwork]] = Field(alias="remoteNetworks",default=None,)

from .networkaccess_web_category import NetworkaccessWebCategory
from .networkaccess_branch_site import NetworkaccessBranchSite
from .networkaccess_remote_network import NetworkaccessRemoteNetwork

