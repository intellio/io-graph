from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCollectInvestigationPackageResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityDeviceIdEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_device_id_entity_identifier import SecurityDeviceIdEntityIdentifier

