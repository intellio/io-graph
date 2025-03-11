from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSFirewallApplication(BaseModel):
	allowsIncomingConnections: Optional[bool] = Field(alias="allowsIncomingConnections",default=None,)
	bundleId: Optional[str] = Field(alias="bundleId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


