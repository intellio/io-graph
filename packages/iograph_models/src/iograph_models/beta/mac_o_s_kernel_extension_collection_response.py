from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSKernelExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MacOSKernelExtension]] = Field(alias="value", default=None,)

from .mac_o_s_kernel_extension import MacOSKernelExtension
