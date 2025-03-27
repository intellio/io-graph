from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIsolateDeviceResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.isolateDeviceResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.isolateDeviceResponseAction")
	identifier: Optional[SecurityDeviceIdEntityIdentifier | str] = Field(alias="identifier", default=None,)
	isolationType: Optional[SecurityIsolationType | str] = Field(alias="isolationType", default=None,)

from .security_device_id_entity_identifier import SecurityDeviceIdEntityIdentifier
from .security_isolation_type import SecurityIsolationType

