from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsActivitySettings(BaseModel):
	urlToItemResolvers: Optional[list[Annotated[Union[ExternalConnectorsItemIdResolver]],Field(discriminator="odata_type")]]] = Field(alias="urlToItemResolvers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_connectors_item_id_resolver import ExternalConnectorsItemIdResolver

