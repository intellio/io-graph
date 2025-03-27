from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Search_existing_identitiesPostRequest(BaseModel):
	importedDeviceIdentities: Optional[list[Annotated[Union[ImportedDeviceIdentityResult]],Field(discriminator="odata_type")]]] = Field(alias="importedDeviceIdentities", default=None,)

from .imported_device_identity_result import ImportedDeviceIdentityResult

