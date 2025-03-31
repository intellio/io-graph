from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class Win32LobAppRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Win32LobAppFileSystemRule, Win32LobAppPowerShellScriptRule, Win32LobAppProductCodeRule, Win32LobAppRegistryRule],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule
from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule
from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule
from .win32_lob_app_registry_rule import Win32LobAppRegistryRule
