from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class External_connectors_add_activitiesPostRequest(BaseModel):
	activities: Optional[list[Annotated[Union[ExternalConnectorsExternalActivityResult],Field(discriminator="odata_type")]]] = Field(alias="activities", default=None,)

from .external_connectors_external_activity_result import ExternalConnectorsExternalActivityResult
