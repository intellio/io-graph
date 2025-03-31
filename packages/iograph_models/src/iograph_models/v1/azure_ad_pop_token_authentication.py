from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class AzureAdPopTokenAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.azureAdPopTokenAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.azureAdPopTokenAuthentication")

