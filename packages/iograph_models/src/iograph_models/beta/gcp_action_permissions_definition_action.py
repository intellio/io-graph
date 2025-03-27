from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class GcpActionPermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.gcpActionPermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.gcpActionPermissionsDefinitionAction")
	actions: Optional[list[str]] = Field(alias="actions", default=None,)


