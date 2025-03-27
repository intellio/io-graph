from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppRequirementCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Win32LobAppFileSystemRequirement, Win32LobAppPowerShellScriptRequirement, Win32LobAppRegistryRequirement]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement
from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement
from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement

