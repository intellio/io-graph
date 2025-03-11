from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedRemoteNetwork(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	remoteNetworkId: Optional[str] = Field(alias="remoteNetworkId",default=None,)


