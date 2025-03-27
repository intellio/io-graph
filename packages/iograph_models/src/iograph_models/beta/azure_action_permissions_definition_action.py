from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AzureActionPermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.azureActionPermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.azureActionPermissionsDefinitionAction")
	actions: Optional[list[str]] = Field(alias="actions", default=None,)


