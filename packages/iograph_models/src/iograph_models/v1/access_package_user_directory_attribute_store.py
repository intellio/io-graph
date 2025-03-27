from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageUserDirectoryAttributeStore(BaseModel):
	odata_type: Literal["#microsoft.graph.accessPackageUserDirectoryAttributeStore"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageUserDirectoryAttributeStore")


